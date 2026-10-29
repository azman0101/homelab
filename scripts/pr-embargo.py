#!/usr/bin/env python3
"""Quarantine PRs using trusted metadata only; never fetch or execute PR code."""
import argparse
from datetime import datetime, timedelta, timezone
import fnmatch
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

MARKER = '<!-- homelab-embargo:v1 '
BOT = 'github-actions[bot]'


def now():
    return datetime.now(timezone.utc)


def timestamp(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Embargo timestamps must include a timezone')
    return result


def relevant(files, policy):
    return any(not any(fnmatch.fnmatchcase(path, pattern)
                       for pattern in policy['excluded_paths']) for path in files)


def state_for(pr, previous, policy, at):
    # Only the head SHA is trusted as an identity, never the upstream release date
    # or an author-controlled commit date. Any push restarts the entire delay.
    if previous and previous.get('sha') == pr['head']['sha']:
        state = dict(previous)
        # A stricter policy cannot be bypassed by keeping an older deadline.
        deadline = timestamp(state['first_seen']) + timedelta(days=policy['days'])
        state['until'] = max(timestamp(state['until']), deadline).isoformat()
        return state
    return {'sha': pr['head']['sha'], 'first_seen': at.isoformat(),
            'until': (at + timedelta(days=policy['days'])).isoformat(),
            'managed_draft': (previous or {}).get('managed_draft', not pr['draft']),
            'released': False, 'dispatched': False}


def eligible(pr, state, at):
    return bool(state and state.get('sha') == pr['head']['sha']
                and at >= timestamp(state['until']))


def read_state(comments):
    matches = []
    for comment in comments:
        if comment['user']['login'] != BOT or comment['user']['type'] != 'Bot':
            continue
        body = comment.get('body') or ''
        if not body.startswith(MARKER):
            continue
        try:
            data = json.loads(body[len(MARKER):body.index(' -->')])
            timestamp(data['first_seen'])
            timestamp(data['until'])
            matches.append((comment['id'], data))
        except (ValueError, KeyError, TypeError):
            continue
    return max(matches, key=lambda item: item[0]) if matches else (None, None)


def body_for(state, policy):
    phase = 'Éligible après embargo' if state['released'] else 'Sous embargo — aucun build de cette PR'
    return (MARKER + json.dumps(state, sort_keys=True) + ' -->\n'
            f'### {phase}\n\n'
            f"- Commit observé : `{state['sha']}`\n"
            f"- Première observation : **{state['first_seen']}**\n"
            f"- Fin au plus tôt : **{state['until']}** (UTC, {policy['days']} jours)\n\n"
            'Tout nouveau commit redémarre le délai. Les labels ne constituent pas une autorisation.\n'
            'La levée rend la PR éligible aux tests ; elle ne fusionne pas la PR et ne certifie pas son innocuité.\n')


class GitHub:
    def __init__(self):
        self.repo = os.environ['GITHUB_REPOSITORY']
        self.api = os.environ.get('GITHUB_API_URL', 'https://api.github.com')

    def request(self, method, path, data=None):
        url = path if path.startswith('https://') else f'{self.api}/repos/{self.repo}/{path}'
        request = urllib.request.Request(url, method=method,
            data=json.dumps(data).encode() if data is not None else None,
            headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                     'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json'})
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
            return json.loads(payload) if payload else None

    def pages(self, path):
        page = 1
        while True:
            separator = '&' if '?' in path else '?'
            values = self.request('GET', f'{path}{separator}per_page=100&page={page}')
            yield from values
            if len(values) < 100:
                return
            page += 1

    def draft(self, pr, draft):
        mutation = 'convertPullRequestToDraft' if draft else 'markPullRequestReadyForReview'
        result = self.request('POST', os.environ.get('GITHUB_GRAPHQL_URL', 'https://api.github.com/graphql'),
            {'query': f'mutation($id: ID!) {{ {mutation}(input: {{pullRequestId: $id}}) {{ pullRequest {{ id }} }} }}',
             'variables': {'id': pr['node_id']}})
        if result.get('errors'):
            raise RuntimeError(json.dumps(result['errors']))


def pull_files(api, number):
    # Include previous names so renaming a protected file into a documentation
    # path cannot turn a supply-chain change into an exemption.
    paths = []
    for item in api.pages(f'pulls/{number}/files'):
        paths.append(item['filename'])
        if item.get('previous_filename'):
            paths.append(item['previous_filename'])
    return paths


def save(api, number, comment_id, state, policy):
    body = body_for(state, policy)
    if comment_id:
        api.request('PATCH', f'issues/comments/{comment_id}', {'body': body})
        return comment_id
    return api.request('POST', f'issues/{number}/comments', {'body': body})['id']


def status(api, pr, policy, state, description):
    api.request('POST', f"statuses/{pr['head']['sha']}", {
        'state': state, 'context': policy['status_context'],
        'description': description[:140], 'target_url': pr['html_url']})


def set_labels(api, number, policy, released):
    add = policy['released_label'] if released else policy['label']
    remove = policy['label'] if released else policy['released_label']
    api.request('POST', f'issues/{number}/labels', {'labels': [add]})
    from urllib.parse import quote
    try:
        api.request('DELETE', f'issues/{number}/labels/{quote(remove, safe="")}')
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise


def authorize(api, number, sha, policy):
    pr = api.request('GET', f'pulls/{number}')
    if pr['state'] != 'open' or pr['draft'] or pr['head']['sha'] != sha:
        raise RuntimeError('PR closed, draft, or head changed; refusing CI')
    if pr['changed_files'] > 3000:
        raise RuntimeError('PR exceeds GitHub file-list limit; refusing CI')
    if relevant(pull_files(api, number), policy):
        _, state = read_state(api.pages(f'issues/{number}/comments'))
        if state:
            state = state_for(pr, state, policy, now())
        if not eligible(pr, state, now()) or not state.get('released'):
            raise RuntimeError('Embargo has not been released for this exact commit; refusing CI')
    return pr


def reconcile(api, number, policy):
    pr = api.request('GET', f'pulls/{number}')
    if pr['state'] != 'open':
        return
    # Fail closed before any metadata requests or GraphQL mutation can fail.
    status(api, pr, policy, 'pending', 'Embargo evaluation in progress; CI is not authorized')
    if pr['changed_files'] > 3000:
        raise RuntimeError('PR exceeds GitHub file-list limit; embargo remains blocked')
    if not relevant(pull_files(api, number), policy):
        _, previous = read_state(api.pages(f'issues/{number}/comments'))
        if previous:
            set_labels(api, number, policy, True)
            if pr['draft'] and previous.get('managed_draft'):
                api.draft(pr, False)
        status(api, pr, policy, 'success', 'Documentation-only change: no supply-chain embargo')
        return
    comment_id, previous = read_state(api.pages(f'issues/{number}/comments'))
    state = state_for(pr, previous, policy, now())
    if not eligible(pr, state, now()):
        state['released'] = False
        state['dispatched'] = False
        save(api, number, comment_id, state, policy)
        set_labels(api, number, policy, False)
        if not pr['draft']:
            api.draft(pr, True)
        status(api, pr, policy, 'pending', f"Under embargo until {state['until']}")
        print(f"PR #{number}: embargo until {state['until']}")
        return
    # Re-fetch before granting approval: a concurrent push must not inherit it.
    current = api.request('GET', f'pulls/{number}')
    if current['head']['sha'] != state['sha'] or current['state'] != 'open':
        print(f'PR #{number}: changed during evaluation; leaving CI blocked')
        return
    state['released'] = True
    comment_id = save(api, number, comment_id, state, policy)
    set_labels(api, number, policy, True)
    if current['draft'] and state['managed_draft']:
        api.draft(current, False)
        current['draft'] = False
    status(api, current, policy, 'success', 'Embargo complete for this exact commit')
    # GITHUB_TOKEN-created ready_for_review events do not trigger PR workflows.
    # Explicit dispatch is intentional and always runs trusted default-branch YAML.
    if not current['draft'] and not state['dispatched']:
        authorize(api, number, state['sha'], policy)
        api.request('POST', 'actions/workflows/validate-images.yml/dispatches', {
            'ref': os.environ['DEFAULT_BRANCH'],
            'inputs': {'pr_number': str(number), 'head_sha': state['sha']}})
        state['dispatched'] = True
        save(api, number, comment_id, state, policy)
    print(f'PR #{number}: eligible; validation dispatched={state["dispatched"]}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['reconcile', 'authorize'])
    parser.add_argument('--number', type=int)
    parser.add_argument('--sha')
    args = parser.parse_args()
    policy = json.loads(Path('.github/embargo.json').read_text())
    if not isinstance(policy['days'], int) or policy['days'] < 1:
        raise ValueError('Embargo must be at least one day')
    api = GitHub()
    if args.mode == 'authorize':
        pr = authorize(api, args.number, args.sha, policy)
        # Metadata values are emitted as data, never interpolated into shell code.
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
            output.write(f"head_sha={pr['head']['sha']}\nbase_sha={pr['base']['sha']}\n")
        return
    for name, color in [(policy['label'], 'd93f0b'), (policy['released_label'], '0e8a16')]:
        try:
            api.request('POST', 'labels', {'name': name, 'color': color})
        except urllib.error.HTTPError as error:
            if error.code != 422:
                raise
    numbers = [args.number] if args.number else [pr['number'] for pr in api.pages('pulls?state=open')]
    errors = []
    for number in numbers:
        try:
            reconcile(api, number, policy)
        except Exception as error:
            errors.append(f'PR #{number}: {error}')
    if errors:
        raise RuntimeError('\n'.join(errors))


if __name__ == '__main__':
    main()
