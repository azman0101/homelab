# Homelab Images

Signed, SBOM-attested, and Trivy-scanned container images for homelab use.

Every image in this repository is:
- 🔒 Built from **digest-pinned** upstream images
- 📋 Equipped with a **SBOM** (CycloneDX + SPDX)
- 🔏 **Signed** with Sigstore/Cosign (keyless, GitHub OIDC)
- 🛡️ **SLSA provenance** verified on every build
- 🔬 **Trivy-scanned** — results visible in the GitHub Security tab

## Images

| Image  | Description | Version  |
|--- |---|--- |
| [home-assistant](./home-assistant) | Home Assistant - Open source home automation | 2026.9.1 |
| [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | 2.1.2-alpine |
| [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | 0.17.2 |
| [caddy](./caddy) | Caddy web server with CrowdSec bouncer | 2.11.4 |
| [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 |
| [authelia](./authelia) | Authelia - open-source authentication and authorization server | 4.39.24 |
| [redis](./redis) | Redis in-memory data store | 8.10.1-alpine |
| [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | 1.2.16 |
| [pihole](./pihole) | Pi-hole - network-wide ad blocking | 2026.07.2 |
| [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | 2.5.3 |
| [influxdb](./influxdb) | InfluxDB - Open-source time-series database | 2.9.1-alpine |

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
