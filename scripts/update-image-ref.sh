#!/usr/bin/env bash
# Maintain the image columns of the root README.md table:
#   | badge | Image | Description | Published | Pending | Pull reference |
#
#   Published       tag actually pushed to GHCR            (written by build-image.yml)
#   Pending         tag declared in the Dockerfile but not yet published, or "—"
#                                                          (written by release-on-bump.yml)
#   Pull reference  `ghcr.io/<owner>/<image>:<tag>@sha256:<digest>` of the published tag
#
# Usage:
#   scripts/update-image-ref.sh published <service> <tag> <digest> [owner]
#   scripts/update-image-ref.sh pending   <service> <tag>
set -euo pipefail

README="${README:-README.md}"
MODE="${1:?mode required: published|pending}"
SERVICE="${2:?service name required}"
TAG="${3:?tag required}"

case "$MODE" in
  published)
    DIGEST="${4:?digest required}"
    OWNER="${5:-${GITHUB_REPOSITORY_OWNER:-azman0101}}"
    if [[ ! "$DIGEST" =~ ^sha256:[0-9a-f]{64}$ ]]; then
      echo "Invalid digest: $DIGEST" >&2
      exit 1
    fi
    REF="ghcr.io/${OWNER,,}/${SERVICE}:${TAG}@${DIGEST}"
    ;;
  pending)
    REF=""
    ;;
  *)
    echo "Unknown mode: $MODE" >&2
    exit 1
    ;;
esac

MODE="$MODE" SRV="$SERVICE" TAG="$TAG" REF="$REF" perl -i -pe '
  BEGIN { $found = 0 }
  $s = $ENV{SRV};
  if (/^(\|\s*!\[[^\]]*\]\([^)]+\)\s*\|\s*\[\Q$s\E\]\(\.\/\Q$s\E\)\s*\|[^|]*\|)([^|]*)\|([^|]*)\|([^|]*)\|\s*$/) {
    ($head, $pub, $pend, $ref) = ($1, $2, $3, $4);
    $pub =~ s/^\s+|\s+$//g;
    $pend =~ s/^\s+|\s+$//g;
    $ref =~ s/^\s+|\s+$//g;
    if ($ENV{MODE} eq "published") {
      $pub = $ENV{TAG};
      $pend = "—" if $pend eq $ENV{TAG};
      $_ = "$head $pub | $pend | `$ENV{REF}` |\n";
    } else {
      $pend = ($pub eq $ENV{TAG}) ? "—" : $ENV{TAG};
      $_ = "$head $pub | $pend | $ref |\n";
    }
    $found = 1;
  }
  END { exit($found ? 0 : 1) }
' "$README" || { echo "Row for '$SERVICE' not found in $README" >&2; exit 1; }

echo "$MODE $SERVICE $TAG"
