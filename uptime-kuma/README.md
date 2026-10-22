# uptime-kuma

Uptime Kuma - Self-hosted monitoring tool

## Upstream image

```
louislam/uptime-kuma:2.5.6@sha256:9912da7d7d9b6ddc0c2d904beb84d24689c1ed9c33b81419eb9008663a92a329
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
cosign verify ghcr.io/${GITHUB_REPOSITORY_OWNER}/uptime-kuma:latest \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

## Verify the SLSA provenance

```bash
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/${GITHUB_REPOSITORY_OWNER}/uptime-kuma:latest
```

## Scan for vulnerabilities

```bash
trivy image ghcr.io/${GITHUB_REPOSITORY_OWNER}/uptime-kuma:latest
```
