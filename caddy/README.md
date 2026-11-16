# caddy

Caddy web server with CrowdSec bouncer

## Upstream image

```
caddy:2.11.9@sha256:0c2243efcf437ab7f7a978f1027fcf0d4f9be8a75df27b1b3fbc5dbe0ffa8cf0
```

## Supply chain security

This image is:
- 🔒 **Built from a digest-pinned upstream** — tag mutation attacks are prevented
- 📋 **SBOM attached** — full software bill of materials via SPDX/CycloneDX
- 🔏 **Signed with Sigstore/cosign** (keyless, OIDC-backed)
- 🛡️ **SLSA provenance** embedded as OCI attestation
- 🔬 **Trivy-scanned** on every build — SARIF results in GitHub Security tab
- 🧪 **Container Structure Tested** — verified binaries, module wiring, and Caddyfile validation

## Verify the signature

```bash
cosign verify ghcr.io/${GITHUB_REPOSITORY_OWNER}/caddy:latest \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

## Verify the SLSA provenance

```bash
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/${GITHUB_REPOSITORY_OWNER}/caddy:latest
```

## Scan for vulnerabilities

```bash
trivy image ghcr.io/${GITHUB_REPOSITORY_OWNER}/caddy:latest
```

## Container structure tests

```bash
container-structure-test test --image ghcr.io/${GITHUB_REPOSITORY_OWNER}/caddy:latest --config caddy/cst.yaml
```
