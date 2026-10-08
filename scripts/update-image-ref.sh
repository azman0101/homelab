#!/usr/bin/env bash
# Update the "Pull reference" column of the root README.md for one service.
#
# Usage: scripts/update-image-ref.sh <service> <tag> <digest> [owner]
#   e.g. scripts/update-image-ref.sh caddy v2.11.6 sha256:abc... azman0101
#
# Result: | ... | ... | ... | ... | `ghcr.io/<owner>/<service>:<tag>@<digest>` |
set -euo pipefail

SERVICE="${1:?service name required}"
TAG="${2:?tag required}"
DIGEST="${3:?digest required}"
OWNER="${4:-${GITHUB_REPOSITORY_OWNER:-azman0101}}"
README="${README:-README.md}"

if [[ ! "$DIGEST" =~ ^sha256:[0-9a-f]{64}$ ]]; then
  echo "Invalid digest: $DIGEST" >&2
  exit 1
fi

REF="ghcr.io/${OWNER,,}/${SERVICE}:${TAG}@${DIGEST}"

SRV="$SERVICE" REF="$REF" perl -i -pe '
  $s = $ENV{SRV}; $r = $ENV{REF};
  if (/^(\|\s*!\[[^\]]*\]\([^)]+\)\s*\|\s*\[\Q$s\E\]\(\.\/\Q$s\E\)\s*\|[^|]*\|[^|]*\|)[^|]*\|\s*$/) {
    $_ = "$1 `$r` |\n";
    $found = 1;
  }
  END { exit($found ? 0 : 1) }
' "$README" || { echo "Row for '$SERVICE' not found in $README" >&2; exit 1; }

echo "$REF"
