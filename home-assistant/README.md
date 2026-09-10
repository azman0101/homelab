# home-assistant

Home Assistant - Open source home automation

## Upstream image

```
ghcr.io/home-assistant/home-assistant:2026.9.1@sha256:612d76760b544cb40b7ba01387fdac964c59a6a550a50a4d30b4773c822d2918
```

## Supply chain security

This image is:
- 🔒 **Built from a digest-pinned upstream** — tag mutation attacks are prevented
- 📋 **SBOM attached** — full software bill of materials via SPDX/CycloneDX
- 🔏 **Signed with Sigstore/cosign** (keyless, OIDC-backed)
- 🛡️ **SLSA provenance** embedded as OCI attestation
- 🔬 **Trivy-scanned** on every build — SARIF results in GitHub Security tab
- 🧪 **Container Structure Tested** — verified image metadata, entrypoint, and essential files

## Verify the signature

```bash
cosign verify ghcr.io/${GITHUB_REPOSITORY_OWNER}/home-assistant:latest \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

## Verify the SLSA provenance

```bash
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp="https://github.com/${GITHUB_REPOSITORY}" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/${GITHUB_REPOSITORY_OWNER}/home-assistant:latest
```

## Scan for vulnerabilities

```bash
trivy image ghcr.io/${GITHUB_REPOSITORY_OWNER}/home-assistant:latest
```

## Container structure tests

```bash
container-structure-test test --image ghcr.io/${GITHUB_REPOSITORY_OWNER}/home-assistant:latest --config home-assistant/cst.yaml
```
