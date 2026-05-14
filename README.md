# Homelab Images

Signed, SBOM-attested, and Trivy-scanned container images for homelab use.

Every image in this repository is:
- 🔒 Built from **digest-pinned** upstream images
- 📋 Equipped with a **SBOM** (CycloneDX + SPDX)
- 🔏 **Signed** with Sigstore/Cosign (keyless, GitHub OIDC)
- 🛡️ **SLSA provenance** verified on every build
- 🔬 **Trivy-scanned** — results visible in the GitHub Security tab

## Images

| Image | Description | Version |
|---|---|---|
| [home-assistant](./home-assistant) | Home Assistant - Open source home automation | 2026.4.2 |
| [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | 2.1.2-alpine |
| [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | 0.17.1 |
| [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.2 |
| [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | latest |
| [authelia](./authelia) | Authelia - open-source authentication and authorization server | 4.39.16 |
| [redis](./redis) | Redis in-memory data store | alpine |
| [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | latest |
| [pihole](./pihole) | Pi-hole - network-wide ad blocking | latest |

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
