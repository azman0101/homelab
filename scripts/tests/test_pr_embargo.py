"""Security regressions; all network calls are mocked. No PR code is executed."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('embargo', ROOT / 'scripts/pr-embargo.py')
e = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(e)
REPO_POLICY = json.loads((ROOT / '.github/embargo.json').read_text())
# Exercise optional Draft support separately from the deployed, disabled policy.
POLICY = dict(REPO_POLICY, manage_drafts=True)
AT = datetime(2026, 10, 29, tzinfo=timezone.utc)


def pr(draft=False, sha='a' * 40):
    return {'number': 1, 'node_id': 'PR_test', 'draft': draft, 'state': 'open',
            'head': {'sha': sha}, 'base': {'sha': 'b' * 40}, 'changed_files': 1,
            'html_url': 'https://github.com/example/repo/pull/1'}


def commit_status(state, context=POLICY['validation_context'], login=e.BOT, at=AT):
    return {'state': state, 'context': context, 'creator': {'login': login},
            'updated_at': at.isoformat().replace('+00:00', 'Z')}


class FakeAPI:
    def __init__(self, pull=None, state=None, files=None, statuses=None, forbid_draft=False):
        self.pull = pull or pr()
        self.comments = [] if state is None else [{
            'id': 10, 'user': {'login': e.BOT, 'type': 'Bot'},
            'body': e.body_for(state, POLICY)}]
        self.files = files or [{'filename': 'caddy/Dockerfile'}]
        self.statuses = list(statuses or [])  # newest first, like the GitHub API
        self.forbid_draft = forbid_draft
        self.calls = []

    def request(self, method, path, data=None):
        self.calls.append((method, path, data))
        if method == 'GET' and path == 'pulls/1':
            return deepcopy(self.pull)
        if path == 'issues/1/comments':
            self.comments.append({'id': 10, 'user': {'login': e.BOT, 'type': 'Bot'},
                                  'body': data['body']})
            return {'id': 10}
        if path == 'issues/comments/10' and method == 'PATCH':
            self.comments[0]['body'] = data['body']
        if method == 'POST' and path.startswith('statuses/'):
            self.statuses.insert(0, commit_status(data['state'], data['context'], at=e.now()))
        return None

    def pages(self, path):
        if path.endswith('/statuses'):
            return iter(self.statuses)
        return iter(self.comments if path.endswith('/comments') else self.files)

    def draft(self, pull, draft):
        self.calls.append(('DRAFT', draft))
        if self.forbid_draft:
            raise e.DraftForbidden('[{"type": "FORBIDDEN"}]')
        self.pull['draft'] = draft


def released(api):
    # authorize re-reads the saved state from GitHub, so emulate that write.
    original_request = api.request
    def request(method, path, data=None):
        result = original_request(method, path, data)
        if path == 'issues/comments/10' and method == 'PATCH':
            api.comments[0]['body'] = data['body']
        return result
    api.request = request
    return api


def dispatches(api):
    return [call for call in api.calls if 'dispatches' in str(call)]


class EmbargoTests(unittest.TestCase):
    def test_first_seen_ignores_commit_and_pr_creation_dates(self):
        pull = pr()
        pull['created_at'] = '2000-01-01T00:00:00Z'
        state = e.state_for(pull, None, POLICY, AT)
        self.assertEqual(e.timestamp(state['until']), AT + timedelta(days=7))
        self.assertFalse(e.eligible(pull, state, AT))

    def test_new_commit_restarts_and_revokes_release(self):
        previous = e.state_for(pr(), None, POLICY, AT)
        previous.update(released=True, dispatched=True)
        updated = pr(sha='c' * 40)
        state = e.state_for(updated, previous, POLICY, AT + timedelta(days=8))
        self.assertEqual(e.timestamp(state['until']), AT + timedelta(days=15))
        self.assertFalse(state['released'])
        self.assertFalse(state['dispatched'])

    def test_same_sha_keeps_clock_and_stricter_policy_extends_it(self):
        state = e.state_for(pr(), None, POLICY, AT)
        self.assertEqual(e.state_for(pr(), state, POLICY, AT + timedelta(days=2)), state)
        longer = dict(POLICY, days=14)
        self.assertEqual(e.timestamp(e.state_for(pr(), state, longer, AT)['until']), AT + timedelta(days=14))

    def test_fake_state_comment_is_ignored(self):
        state = e.state_for(pr(), None, POLICY, AT)
        comments = [{'id': 99, 'user': {'login': 'attacker', 'type': 'User'},
                     'body': e.body_for(state, POLICY)}]
        self.assertEqual(e.read_state(comments), (None, None))

    def test_docs_exempt_but_scripts_workflows_new_files_are_not(self):
        self.assertFalse(e.relevant(['README.md', 'caddy/README.md', '.github/badges/caddy.svg'], POLICY))
        for path in ['caddy/Dockerfile', '.github/workflows/caddy.yml', 'scripts/tool.py', 'new-dependency.lock']:
            self.assertTrue(e.relevant([path], POLICY))

    @patch.object(e, 'now', return_value=AT)
    def test_opening_or_manually_readying_pr_never_dispatches(self, _):
        for previous in [None, e.state_for(pr(), None, POLICY, AT)]:
            api = FakeAPI(state=previous)
            e.reconcile(api, 1, POLICY)
            self.assertIn(('DRAFT', True), api.calls)
            self.assertFalse(any('dispatches' in str(call) for call in api.calls))
            states = [call[2]['state'] for call in api.calls if len(call) == 3 and call[1].startswith('statuses/')]
            self.assertTrue(all(state == 'pending' for state in states))

    @patch.object(e, 'now', return_value=AT + timedelta(days=7))
    def test_expiry_marks_ready_and_dispatches_trusted_main_once(self, _):
        state = e.state_for(pr(), None, POLICY, AT)
        api = released(FakeAPI(pull=pr(draft=True), state=state))
        with patch.dict(e.os.environ, DEFAULT_BRANCH='main'):
            e.reconcile(api, 1, POLICY)
            e.reconcile(api, 1, POLICY)
        dispatches = [call for call in api.calls if 'dispatches' in str(call)]
        self.assertEqual(len(dispatches), 1)
        self.assertEqual(dispatches[0][2]['ref'], 'main')
        self.assertEqual(dispatches[0][2]['inputs']['head_sha'], pr()['head']['sha'])
        self.assertIn(('DRAFT', False), api.calls)

    @patch.object(e, 'now', return_value=AT + timedelta(days=30))
    def test_authorize_rejects_wrong_sha_unreleased_draft_closed_and_missing_state(self, _):
        state = e.state_for(pr(), None, POLICY, AT)
        state['released'] = True
        for pull, saved, sha in [(pr(), None, 'a'*40), (pr(), state, 'c'*40),
                                 (pr(draft=True), state, 'a'*40),
                                 (dict(pr(), state='closed'), state, 'a'*40),
                                 (pr(), dict(state, released=False), 'a'*40)]:
            with self.assertRaises(RuntimeError):
                e.authorize(FakeAPI(pull=pull, state=saved), 1, sha, POLICY)

    def test_renamed_protected_file_cannot_hide_as_documentation(self):
        api = FakeAPI(files=[{'filename': 'README.md', 'previous_filename': 'caddy/Dockerfile'}])
        self.assertTrue(e.relevant(e.pull_files(api, 1), POLICY))

    @patch.object(e, 'now', return_value=AT + timedelta(days=8))
    def test_auth_checks_updated_policy_and_deadline_even_if_released(self, _):
        state = e.state_for(pr(), None, POLICY, AT)
        state['released'] = True
        api = FakeAPI(state=state)
        with self.assertRaises(RuntimeError):
            e.authorize(api, 1, pr()['head']['sha'], dict(POLICY, days=14))

    @patch.object(e, 'now', return_value=AT + timedelta(days=8))
    def test_original_author_draft_is_not_readied_or_built_on_expiry(self, _):
        state = e.state_for(pr(draft=True), None, POLICY, AT)
        api = FakeAPI(pull=pr(draft=True), state=state)
        e.reconcile(api, 1, POLICY)
        self.assertNotIn(('DRAFT', False), api.calls)
        self.assertFalse(any('dispatches' in str(call) for call in api.calls))

    @patch.object(e, 'now', return_value=AT + timedelta(days=8))
    def test_concurrent_push_cannot_receive_old_release(self, _):
        state = e.state_for(pr(), None, POLICY, AT)
        api = FakeAPI(state=state)
        original_request = api.request
        gets = 0
        def request(method, path, data=None):
            nonlocal gets
            if method == 'GET' and path == 'pulls/1':
                gets += 1
                if gets == 2:
                    api.pull['head']['sha'] = 'c' * 40
            return original_request(method, path, data)
        api.request = request
        e.reconcile(api, 1, POLICY)
        self.assertFalse(any('dispatches' in str(call) for call in api.calls))

    @patch.object(e, 'now', return_value=AT)
    def test_forbidden_draft_conversion_keeps_embargo_without_failing(self, _):
        api = FakeAPI(forbid_draft=True)
        e.reconcile(api, 1, POLICY)
        self.assertIn(('DRAFT', True), api.calls)
        self.assertEqual(api.statuses[0]['context'], POLICY['status_context'])
        self.assertEqual(api.statuses[0]['state'], 'pending')
        self.assertFalse(dispatches(api))

    @patch.object(e, 'now', return_value=AT)
    def test_forbidden_draft_is_not_retried_even_after_new_commit(self, _):
        api = FakeAPI(forbid_draft=True)
        e.reconcile(api, 1, POLICY)
        e.reconcile(api, 1, POLICY)
        api.pull['head']['sha'] = 'c' * 40
        e.reconcile(api, 1, POLICY)
        self.assertEqual(api.calls.count(('DRAFT', True)), 1)
        _, state = e.read_state(api.comments)
        self.assertTrue(state['draft_forbidden'])
        self.assertEqual(state['sha'], 'c' * 40)
        self.assertEqual(api.statuses[0]['state'], 'pending')
        self.assertFalse(dispatches(api))

    @patch.object(e, 'now', return_value=AT)
    def test_deployed_policy_never_attempts_draft_conversion(self, _):
        self.assertIs(REPO_POLICY['manage_drafts'], False)
        api = FakeAPI(forbid_draft=True)
        with patch('builtins.print') as output:
            e.reconcile(api, 1, REPO_POLICY)
            e.reconcile(api, 1, REPO_POLICY)
        self.assertFalse(any(call[0] == 'DRAFT' for call in api.calls))
        self.assertFalse(any('warning' in str(call) for call in output.call_args_list))
        self.assertEqual(api.statuses[0]['state'], 'pending')
        self.assertFalse(dispatches(api))

    def test_remembered_refusal_also_prevents_ready_mutation(self):
        state = dict(e.state_for(pr(), None, POLICY, AT), draft_forbidden=True)
        api = FakeAPI(pull=pr(draft=True))
        self.assertFalse(e.set_draft(api, api.pull, False, POLICY, state, 10))
        self.assertEqual(api.calls, [])

    def test_non_permission_error_is_not_silently_cached(self):
        api = FakeAPI()
        state = e.state_for(pr(), None, POLICY, AT)
        with patch.object(api, 'draft', side_effect=RuntimeError('temporary failure')):
            with self.assertRaises(RuntimeError):
                e.set_draft(api, api.pull, True, POLICY, state, 10)
        self.assertFalse(state['draft_forbidden'])

    @patch.object(e, 'now', return_value=AT + timedelta(days=7))
    def test_release_dispatches_even_if_draft_cannot_be_changed(self, _):
        state = e.state_for(pr(), None, POLICY, AT)
        api = released(FakeAPI(state=state, forbid_draft=True))
        with patch.dict(e.os.environ, DEFAULT_BRANCH='main'):
            e.reconcile(api, 1, POLICY)
        self.assertEqual(len(dispatches(api)), 1)
        contexts = {(s['context'], s['state']) for s in api.statuses}
        self.assertIn((POLICY['status_context'], 'success'), contexts)
        self.assertIn((POLICY['validation_context'], 'pending'), contexts)

    def test_validation_is_retried_only_when_it_never_reported(self):
        at = AT + timedelta(days=8)
        cases = [([], 1),
                 ([commit_status('pending', at=at - timedelta(hours=4))], 1),
                 ([commit_status('pending', at=at - timedelta(hours=1))], 0),
                 ([commit_status('failure', at=at - timedelta(hours=4))], 0),
                 ([commit_status('success', at=at - timedelta(hours=4))], 0),
                 ([commit_status('success', login='attacker')], 1)]
        for statuses, expected in cases:
            state = dict(e.state_for(pr(), None, POLICY, AT), released=True, dispatched=True)
            api = released(FakeAPI(state=state, statuses=statuses))
            with patch.object(e, 'now', return_value=at), patch.dict(e.os.environ, DEFAULT_BRANCH='main'):
                e.reconcile(api, 1, POLICY)
            self.assertEqual(len(dispatches(api)), expected, statuses)

    @patch.object(e, 'now', return_value=AT)
    def test_docs_only_change_satisfies_both_required_statuses(self, _):
        api = FakeAPI(files=[{'filename': 'docs/embargo.md'}, {'filename': 'README.md'}])
        e.reconcile(api, 1, POLICY)
        latest = {}
        for item in reversed(api.statuses):  # oldest first, so the newest wins
            latest[item['context']] = item['state']
        self.assertEqual(latest, {POLICY['status_context']: 'success',
                                  POLICY['validation_context']: 'success'})
        self.assertFalse(dispatches(api))

    @patch.object(e, 'now', return_value=AT)
    def test_large_pr_fails_closed(self, _):
        api = FakeAPI(pull=dict(pr(), changed_files=3001))
        with self.assertRaises(RuntimeError):
            e.reconcile(api, 1, POLICY)
        self.assertFalse(any('dispatches' in str(call) for call in api.calls))


if __name__ == '__main__':
    unittest.main()
