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
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/home-assistant.yml?branch=main&label=published) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.10.0 | — | `ghcr.io/azman0101/home-assistant:v2026.10.0@sha256:b6864ff4496ea14bf795f5f6502788ef3dccd37523ee4858db472ac9017eac4b` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/mosquitto.yml?branch=main&label=published) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:b5ea8d875fcd0de0952697f4da3698e29a157e34f6c3d956e67e611ccb32559f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/frigate.yml?branch=main&label=published) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.0 | — | `ghcr.io/azman0101/frigate:v0.18.0@sha256:5d1771cf6e9c147d0a2f1213d4a69827626b0ff31c84a373cf148547c82b36dd` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/caddy.yml?branch=main&label=published) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.6 | — | `ghcr.io/azman0101/caddy:v2.11.6@sha256:7c60fd6130c5d92f05d7fbd7004a8b9d3c163a583dbd75bcea7e2a30040005b5` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/crowdsec.yml?branch=main&label=published) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | — | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:e847cbcd685c03be20f8cce1fb8b471d6f611f41aaa840f40d1ae8503d991f0b` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/authelia.yml?branch=main&label=published) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:fde37b60ea133f7d72f374cef01d1fbedc1de211724811d7cb0cbd39d8cd7878` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/redis.yml?branch=main&label=published) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:6733dc0d6215f19f4c38fc929c3fd3f313b7b64a58cda0b3a71877a8aadb1f86` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/postfix-relay.yml?branch=main&label=published) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:ccbbc9f7f19ccbe5a307f6ebd809093487764da829e59736f97f21a33bdec31f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/pihole.yml?branch=main&label=published) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.09.0 | — | `ghcr.io/azman0101/pihole:v2026.09.0@sha256:4a7c9f62f87b24c510ecd37a6d830a4c379a2756e5938685769647cd76c3dc7b` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/uptime-kuma.yml?branch=main&label=published) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.5 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.5@sha256:7c89727d537995173b46cbbf84e165466ff764fbe7793b764152131e18a243b9` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/influxdb.yml?branch=main&label=published) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:bfef800c937e9c8db7a1a717399de94db1a79c021ab037e84c7c1fd709d8c468` |

- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
