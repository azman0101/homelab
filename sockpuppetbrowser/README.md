# Browser backend for changedetection.io

## Upstream image

```
dgtlmoon/sockpuppetbrowser:0.0.3@sha256:23a7be698216407648b6c78fc55de0411bde550635edc30347373c86a5176fad
```

Published as `ghcr.io/azman0101/sockpuppetbrowser:v0.0.3@sha256:<published-digest>`.
Use the complete reference recorded in the root README after publication.
The image preserves upstream files, entrypoint and defaults. No deployment data
or credentials are included.

## Validation

The pull-request workflow builds this image, runs the smoke check and scans
fixable HIGH/CRITICAL findings with Trivy. Main publication uses the existing
shared build, structure-test, SBOM, provenance and Cosign pipeline.

## Deployment gate

Release 0.0.3 is from August 2025 and uses Chromium 119. It is older than the
September 2026 image currently on the NVR. This PR must remain draft while the
security or compatibility checks fail. Do not deploy it merely because it has
a numbered release. The isolated compatibility test uses changedetection 0.60.9
as the Playwright client and performs JavaScript rendering and a screenshot.

## Security result on 2026-10-23

Trivy 0.76.1 reports **3 fixable CRITICAL and 57 fixable HIGH** findings in the
pinned upstream image (OS and application dependencies, unfixed findings excluded).
This release fails the deployment gate and must not replace the current NVR browser.

Critical findings:
- `CVE-2024-32002` — `git` 2.40.1-r0; fixed: 2.40.3-r0.
- `CVE-2024-56171` — `libxml2` 2.11.6-r0; fixed: 2.11.8-r1.
- `GHSA-6q48-6c7w-9gw2` — `certifi` 2025.8.3; fixed: 2026.10.19.
