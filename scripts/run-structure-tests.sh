#!/usr/bin/env bash
# Run the Container Structure Tests of a service against an image already
# present in the local Docker daemon (pulled or freshly built).
#
# Usage: scripts/run-structure-tests.sh <service> <image-ref>
#
# The config is discovered as <service>/cst.yaml, container-structure-test.yaml
# or container-structure-test.yml. Without one, the tests are skipped.
set -euo pipefail

SERVICE="${1:?service name required}"
IMAGE_REF="${2:?image reference required}"

CST_IMAGE_TAG="gcr.io/gcp-runtimes/container-structure-test:v1.16.0"
# Update CST_BINARY_SHA256 whenever CST_IMAGE_TAG is bumped (linux/amd64 digest of the binary inside the image)
CST_BINARY_SHA256="9cc21a2dbe6f72a6a10195cc3b6fd1db5eb76c4aaeac09b42b06a6f017f4de4a"
CST_BIN="${RUNNER_TEMP:-/tmp}/container-structure-test"

CST_CONFIG=""
for f in "${SERVICE}/cst.yaml" "${SERVICE}/container-structure-test.yaml" "${SERVICE}/container-structure-test.yml"; do
  if [ -f "$f" ]; then
    CST_CONFIG="$f"
    break
  fi
done

if [ -z "$CST_CONFIG" ]; then
  echo "No Container Structure Test config found for ${SERVICE}, skipping."
  exit 0
fi

echo "Found Container Structure Test config: ${CST_CONFIG}"
if [ ! -x "$CST_BIN" ] || ! echo "${CST_BINARY_SHA256}  ${CST_BIN}" | sha256sum -c - >/dev/null 2>&1; then
  docker pull "${CST_IMAGE_TAG}"
  CST_CONTAINER_ID=$(docker create "${CST_IMAGE_TAG}")
  docker cp "${CST_CONTAINER_ID}:/container-structure-test" "${CST_BIN}"
  docker rm "${CST_CONTAINER_ID}" >/dev/null
  chmod +x "${CST_BIN}"
fi
echo "${CST_BINARY_SHA256}  ${CST_BIN}" | sha256sum -c -
"${CST_BIN}" test --image "${IMAGE_REF}" --config "${CST_CONFIG}"
