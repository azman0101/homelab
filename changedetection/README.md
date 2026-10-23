# Website change detection

## Upstream image

```
ghcr.io/dgtlmoon/changedetection.io:0.60.9@sha256:04eaae7915bad711160cb15abe160f6d3fabe98bbbd658509d4b7a654000fb2d
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
