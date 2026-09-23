# pihole

Pi-hole - network-wide ad blocking

## Upstream image

```
pihole/pihole:2026.09.0@sha256:5b9c8cf51de7d6d3f2240dbe72baf5f06e1fd39cb4d77a99fab4fa13e23bd1be
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
cosign verify ghcr.io/${GITHUB_REPOSITORY_OWNER}/pihole:latest \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

## Verify the SLSA provenance

```bash
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/${GITHUB_REPOSITORY_OWNER}/pihole:latest
```

## Scan for vulnerabilities

```bash
trivy image ghcr.io/${GITHUB_REPOSITORY_OWNER}/pihole:latest
```
