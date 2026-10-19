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
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/home-assistant.yml?branch=main&label=published) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.10.0 | — | `ghcr.io/azman0101/home-assistant:v2026.10.0@sha256:dffcd868338ee2f16c193e21326679476496f74a08293514865c56c92f72c27f` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/mosquitto.yml?branch=main&label=published) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:5028b098460998f4661f1142b39772b918b7489f7a4f7963f49274aa1fa4f560` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/frigate.yml?branch=main&label=published) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:b0482769717a2166236beab12d34a3b25fa568b0280c6f56a06828f38e600349` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/caddy.yml?branch=main&label=published) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.6 | — | `ghcr.io/azman0101/caddy:v2.11.6@sha256:606d1c5bf239f0e5407fbff9ee3a0df3b51d8a392472d77af86a7d9d4db8d73e` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/crowdsec.yml?branch=main&label=published) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | — | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:4b426a85f4df69e3f5a0a078d23d1b81a805a03c6f0c2fc9309f7bdfb2f746d4` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/authelia.yml?branch=main&label=published) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:3bd8d3e3c750f521e25b12702ce21f30bb48e0fe8b35e1eacf5ea2478e290d97` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/redis.yml?branch=main&label=published) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:f6ba1778c9a9f6dc6cfeccc5aa9292f85a8f8837dd5efc4faf2e7a8fba7f3c40` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/postfix-relay.yml?branch=main&label=published) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:69ac3908f58c8f2eb0d5f8211ecaf5ab4a3ed625379f5588fa4dd876620c35b5` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/pihole.yml?branch=main&label=published) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.09.0 | — | `ghcr.io/azman0101/pihole:v2026.09.0@sha256:2b3feb1fff0bb89517be8ec693b40d8f560fe695348e64c6125eea4bb6d04904` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/uptime-kuma.yml?branch=main&label=published) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.5 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.5@sha256:d52b48c8eedd2254a506159d110241e879c93d6b1f0abb040c0fc11d5ba1e652` |
| ![published](https://img.shields.io/github/actions/workflow/status/azman0101/homelab/influxdb.yml?branch=main&label=published) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:c945726cf24b80e18a9359ccd17aeacbe25bba1662ec4cc2f0ded9c34c5bb9f6` |

- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
