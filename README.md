# Homelab Images

Signed, SBOM-attested, and Trivy-scanned container images for homelab use.

Every image in this repository is:
- 🔒 Built from **digest-pinned** upstream images
- 📋 Equipped with a **SBOM** (CycloneDX + SPDX)
- 🔏 **Signed** with Sigstore/Cosign (keyless, GitHub OIDC)
- 🛡️ **SLSA provenance** verified on every build
- 🔬 **Trivy-scanned** — results visible in the GitHub Security tab

## Images

| Built & Published | Image | Description | Version | Pull reference (`tag@digest`) |
|---|---|---|---|---|
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/home-assistant.yml?branch=main&label=published) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | 2026.10.0 | _pending next build_ |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/mosquitto.yml?branch=main&label=published) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | 2.1.2-alpine | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:f8c5ee73925b1953e30785187b3df3473388373b0bca5d72293271d29d7bb005` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/frigate.yml?branch=main&label=published) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | 0.18.0 | `ghcr.io/azman0101/frigate:v0.18.0@sha256:5d1771cf6e9c147d0a2f1213d4a69827626b0ff31c84a373cf148547c82b36dd` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/caddy.yml?branch=main&label=published) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | 2.11.6 | _pending next build_ |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/crowdsec.yml?branch=main&label=published) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:11a42b9963b4592f3938ed20a1c0e43501bd96e6068a3a443f323319103058eb` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/authelia.yml?branch=main&label=published) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | 4.39.28 | `ghcr.io/azman0101/authelia:v4.39.28@sha256:052870406edaf7c66193f95bd8b1fba7acebe96ac1c3f4fb459ea0b30a8ff26f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/redis.yml?branch=main&label=published) | [redis](./redis) | Redis in-memory data store | 8.10.2-alpine | _pending next build_ |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/postfix-relay.yml?branch=main&label=published) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | 1.2.17 | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:8d6cdf3ef992106d962f319db25736013b9f72004d0bda0812e3a566a05222ac` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/pihole.yml?branch=main&label=published) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | 2026.09.0 | `ghcr.io/azman0101/pihole:v2026.09.0@sha256:fc1aeae3efc60002259eedb74bd334a0288714241ea9573f72f6657b384ecb9c` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/uptime-kuma.yml?branch=main&label=published) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | 2.5.5 | `ghcr.io/azman0101/uptime-kuma:v2.5.5@sha256:67da64636678779a9f04d970d12e7f29dc8be5a23fc63bf9680506a9df3f28a4` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/influxdb.yml?branch=main&label=published) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | 2.9.1-alpine | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:c14a7e6e7a7f6a46f60613efe13c2a0c8b9b17612c1285d18b39b9badb4578bb` |

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
