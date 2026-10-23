# Portainer Community Edition

## Upstream image

```
portainer/portainer-ce:2.45.3@sha256:3609c307943bca8e5c492f69ddd6965df177208b50678a4cff28391c8dd4e96e
```

Published as `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:<published-digest>`.
Use the complete reference recorded in the root README after publication.
The image preserves upstream files, entrypoint and defaults. No deployment data
or credentials are included.

## Validation

The pull-request workflow builds this image, runs the smoke check and scans
fixable HIGH/CRITICAL findings with Trivy. Main publication uses the existing
shared build, structure-test, SBOM, provenance and Cosign pipeline.

Back up `portainer_data` with Portainer stopped before upgrading. Database
migrations require the matching pre-upgrade data backup for rollback. Preserve
the existing volume, Docker socket and published ports when recreating the server.
