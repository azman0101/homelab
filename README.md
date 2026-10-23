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
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/home-assistant.yml?branch=main&label=published) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.10.2 | — | `ghcr.io/azman0101/home-assistant:v2026.10.2@sha256:701b7216b9187e4a86a8f162fc07fa8a2b02c3429e6734f17e2f9acb8a9797cd` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/mosquitto.yml?branch=main&label=published) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:9eebe31ee6091a753f1fc9f841b0447069cd3632c0a05de56bfd9909ccc56201` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/frigate.yml?branch=main&label=published) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:bacb4d542e52d05c6a76eeb9f8eb9f0be154bb1386fd5082aed5071e31627e1f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/caddy.yml?branch=main&label=published) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.7 | — | `ghcr.io/azman0101/caddy:v2.11.7@sha256:d3777602ab7aed778bc7655b45f8687ab7f5553765e47abd7bab02b94bb7f83b` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/crowdsec.yml?branch=main&label=published) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | — | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:46f1905a0a6a624666c3f0652abccd9942cac51cb55751b0071b4b4bfe722f5a` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/authelia.yml?branch=main&label=published) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:ce4c48e4237113d8fdc156532ab15f1733efe753b1b09e1e881cfd88ee85b3bb` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/redis.yml?branch=main&label=published) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:c501d2e526d7e31f90b3d033e4978bd9f564e4dea1effded31191d7113bd0343` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/postfix-relay.yml?branch=main&label=published) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:15d2fe3b0ae046b010f0812eee4878887dcf654c964335bab0c8a4562ea8b948` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/pihole.yml?branch=main&label=published) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.10.0 | — | `ghcr.io/azman0101/pihole:v2026.10.0@sha256:d7c7b0431879726e0ad30d7a14fe3827fd0ba4688f8c537bbf4c045bfac277ae` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/uptime-kuma.yml?branch=main&label=published) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.6 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.6@sha256:c22c2f8eac7ab75ba44b0b5485343407a6a6efc6309e78711f9b825b35aa0395` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/influxdb.yml?branch=main&label=published) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:761e3884b13dfaed3abb669af69b60349e5684e7e5de96856a7ad7cf1510b456` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/changedetection.yml?branch=main&label=published) | [changedetection](./changedetection) | Website change detection | — | v0.60.9 | — |

- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
