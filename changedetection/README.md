# Website change detection

## Upstream image

```
ghcr.io/dgtlmoon/changedetection.io:0.70.3@sha256:47b1e9cc3eff820e6022b655e3fcc948625f60c1770ae8b9c30aa3bf104dc255
```

Published as `ghcr.io/azman0101/changedetection:v0.60.9@sha256:<published-digest>`.
Use the complete reference recorded in the root README after publication.
The image preserves upstream files, entrypoint and defaults. No deployment data
or credentials are included.

## Validation

The pull-request workflow builds this image, runs the smoke check and scans
fixable HIGH/CRITICAL findings with Trivy. Main publication uses the existing
shared build, structure-test, SBOM, provenance and Cosign pipeline.

Back up `/datastore` before upgrading from a development build. Test browser
compatibility on an isolated datastore without production notification targets.
