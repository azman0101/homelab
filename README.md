# Homelab Images

Signed, SBOM-attested, and Trivy-scanned container images for homelab use.

Every image in this repository is:
- 🔒 Built from **digest-pinned** upstream images
- 📋 Equipped with a **SBOM** (CycloneDX + SPDX)
- 🔏 **Signed** with Sigstore/Cosign (keyless, GitHub OIDC)
- 🛡️ **SLSA provenance** verified on every build
- 🔬 **Trivy-scanned** — results visible in the GitHub Security tab

## Images

| Built & Published | Image | Description | Published | Pending | Pull reference (`tag@digest`) |
|---|---|---|---|---|---|
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/home-assistant.yml?branch=main&label=published) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.10.4 | — | `ghcr.io/azman0101/home-assistant:v2026.10.4@sha256:70b3adbaf9a5b9bb64c07c9398f7163f5c91128b83915095962592c87f4a96cf` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/mosquitto.yml?branch=main&label=published) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:75d7356381dbbf72c9ab58af2e37b5a1155d637fa1cd4a754ea5128b1b0814df` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/frigate.yml?branch=main&label=published) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:cd92a9a52f6d3a8c2c10ef46e99a78e86af71fe2f51bc0f69064359df3a394e9` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/caddy.yml?branch=main&label=published) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.7 | — | `ghcr.io/azman0101/caddy:v2.11.7@sha256:b0aa7104be32afeb85b6fdac3484d5e0b034829c04e2b8578665efba9fdf27ad` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/crowdsec.yml?branch=main&label=published) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | — | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:ce77120a35648fe39e5b521a5053c18ccc051e6a6b2b5f6cedd71b8bd009365e` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/authelia.yml?branch=main&label=published) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:d578012132aa661431554944e26cffd00636b79fbb78462632779caf3d470164` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/redis.yml?branch=main&label=published) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:86cd2a9ce10deed0cb1cf1d4e1df156c6adbae953b8ebe1163c347d3b5881393` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/postfix-relay.yml?branch=main&label=published) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:07dd738564e4dc1bb312177663d87d0b8cee7f652bc2f6590b7aafe562889911` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/pihole.yml?branch=main&label=published) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.10.0 | — | `ghcr.io/azman0101/pihole:v2026.10.0@sha256:0d3076d173251a7c25923596dc7203faf4ce489ad0497d8f265a4cf46c73cf2f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/uptime-kuma.yml?branch=main&label=published) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.6 | v2.5.7 | `ghcr.io/azman0101/uptime-kuma:v2.5.6@sha256:ed8a5a071a2dc73dbcc113a47b16678c3fa1accce89986eace9ee94bc15285b1` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/influxdb.yml?branch=main&label=published) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:409eba76ca9c87eff9fde275f4d74dd60451daa60e103c53e01555fca3e8d8ed` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/portainer-ce.yml?branch=main&label=published) | [portainer-ce](./portainer-ce) | Portainer Community Edition | v2.45.3 | — | `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:74e6dcf374b569412288d4fffafd37d48e35d2bde826297181434826d9e8e89f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/changedetection.yml?branch=main&label=published) | [changedetection](./changedetection) | Website change detection | v0.60.10 | — | `ghcr.io/azman0101/changedetection:v0.60.10@sha256:d8e46de6b1a263c8828fedcb8c046aa2c0219621f98c8b3db7df3c8b678d9f52` |

- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
