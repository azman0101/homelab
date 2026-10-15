# frigate

Frigate NVR - Network Video Recorder with local AI object detection

## Upstream image

```
ghcr.io/blakeblackshear/frigate:0.18.1@sha256:ae4ee2505e4dba6313b02bf5e8eea6c35fb1119f7087b9f684082be0a9fa0a71
```

## Supply chain security

This image is:
- 🔒 **Built from a digest-pinned upstream** — tag mutation attacks are prevented
- 📋 **SBOM attached** — full software bill of materials via SPDX/CycloneDX
- 🔏 **Signed with Sigstore/cosign** (keyless, OIDC-backed)
- 🛡️ **SLSA provenance** embedded as OCI attestation
- 🔬 **Trivy-scanned** on every build — SARIF results in GitHub Security tab

## Verify the signature

```bash
cosign verify ghcr.io/${GITHUB_REPOSITORY_OWNER}/frigate:latest \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

## Verify the SLSA provenance

```bash
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/${GITHUB_REPOSITORY_OWNER}/frigate:latest
```

## Scan for vulnerabilities

```bash
trivy image ghcr.io/${GITHUB_REPOSITORY_OWNER}/frigate:latest
```
