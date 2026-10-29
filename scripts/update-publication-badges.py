#!/usr/bin/env python3
"""Render publication badges from the newest run, without branch/event filters."""
import html
import json
import os
from pathlib import Path
import urllib.request


def request(path):
    req = urllib.request.Request(
        f"{os.environ.get('GITHUB_API_URL', 'https://api.github.com')}/repos/{os.environ['GITHUB_REPOSITORY']}/{path}",
        headers={"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
                 "Accept": "application/vnd.github+json"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def render(run):
    state = (run.get('conclusion') or 'unknown') if run['status'] == 'completed' else run['status']
    color = {'success': '#4c1', 'failure': '#e05d44', 'startup_failure': '#e05d44',
             'timed_out': '#e05d44', 'action_required': '#e05d44',
             'in_progress': '#dfb317', 'queued': '#dfb317', 'requested': '#dfb317',
             'waiting': '#dfb317', 'pending': '#dfb317'}.get(state, '#9f9f9f')
    message = state.replace('_', ' ')
    right = max(56, len(message) * 7 + 16)
    width = 70 + right
    label = html.escape(f"published: {message}", quote=True)
    desc = html.escape(f"{run['html_url']} ({run['head_branch']})", quote=True)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" role="img" aria-label="{label}">
  <title>{label}</title><desc>{desc}</desc>
  <rect width="70" height="20" fill="#555"/><rect x="70" width="{right}" height="20" fill="{color}"/>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11">
    <text x="35" y="14">published</text><text x="{70 + right / 2:g}" y="14">{html.escape(message)}</text>
  </g>
</svg>
'''


def main():
    output = Path('.github/badges')
    output.mkdir(parents=True, exist_ok=True)
    # Workflow file names come from trusted default-branch Dockerfile directories.
    # Do not execute or check out code/artifacts from the triggering run.
    for dockerfile in sorted(Path('.').glob('*/Dockerfile')):
        service = dockerfile.parent.name
        runs = request(f'actions/workflows/{service}.yml/runs?per_page=1')['workflow_runs']
        if not runs:
            raise RuntimeError(f'No workflow runs found for {service}')
        (output / f'{service}.svg').write_text(render(runs[0]), encoding='utf-8')
        print(f"{service}: {runs[0]['status']} / {runs[0].get('conclusion')}")


if __name__ == '__main__':
    main()
