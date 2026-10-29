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
| [![published](./.github/badges/home-assistant.svg)](https://github.com/azman0101/homelab/actions/workflows/home-assistant.yml) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.10.4 | — | `ghcr.io/azman0101/home-assistant:v2026.10.4@sha256:e4e12374c0aaacb2fb1d62acf9675e59e3d4a3a052aa32619ba57f16da108bfb` |
| [![published](./.github/badges/mosquitto.svg)](https://github.com/azman0101/homelab/actions/workflows/mosquitto.yml) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:75d7356381dbbf72c9ab58af2e37b5a1155d637fa1cd4a754ea5128b1b0814df` |
| [![published](./.github/badges/frigate.svg)](https://github.com/azman0101/homelab/actions/workflows/frigate.yml) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:693c960d66c46adad14edd05ce2d6790379b8324a45380073a6f020bc73190be` |
| [![published](./.github/badges/caddy.svg)](https://github.com/azman0101/homelab/actions/workflows/caddy.yml) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.7 | — | `ghcr.io/azman0101/caddy:v2.11.7@sha256:9a282056cb1b7400ad523b522dc0192ee51a8855d5a795f7272970dcef7528f0` |
| [![published](./.github/badges/crowdsec.svg)](https://github.com/azman0101/homelab/actions/workflows/crowdsec.yml) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | — | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:ce77120a35648fe39e5b521a5053c18ccc051e6a6b2b5f6cedd71b8bd009365e` |
| [![published](./.github/badges/authelia.svg)](https://github.com/azman0101/homelab/actions/workflows/authelia.yml) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:38f4eb42812c527e9b9160ee62d901ce769ac52b962b2c88bfd5807698b2284b` |
| [![published](./.github/badges/redis.svg)](https://github.com/azman0101/homelab/actions/workflows/redis.yml) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:86cd2a9ce10deed0cb1cf1d4e1df156c6adbae953b8ebe1163c347d3b5881393` |
| [![published](./.github/badges/postfix-relay.svg)](https://github.com/azman0101/homelab/actions/workflows/postfix-relay.yml) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:268d0ecc8686ed762fc04e233e086f77a297868789a3a5674b422f2fa63f3eaf` |
| [![published](./.github/badges/pihole.svg)](https://github.com/azman0101/homelab/actions/workflows/pihole.yml) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.10.0 | — | `ghcr.io/azman0101/pihole:v2026.10.0@sha256:8908e562b41f584eea12b0f6b2f01798efe8014af1da455c0aa5336d405859f3` |
| [![published](./.github/badges/uptime-kuma.svg)](https://github.com/azman0101/homelab/actions/workflows/uptime-kuma.yml) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.7 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.7@sha256:c365b24a44ac5374dec9e4425db18615e8eab78533f21b3adfd52f4072c22406` |
| [![published](./.github/badges/influxdb.svg)](https://github.com/azman0101/homelab/actions/workflows/influxdb.yml) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:3475c7794c543375f1cca07dfa0c592237b82b010a653ec3a582a34a3ac30871` |
| [![published](./.github/badges/portainer-ce.svg)](https://github.com/azman0101/homelab/actions/workflows/portainer-ce.yml) | [portainer-ce](./portainer-ce) | Portainer Community Edition | v2.45.3 | — | `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:74e6dcf374b569412288d4fffafd37d48e35d2bde826297181434826d9e8e89f` |
| [![published](./.github/badges/changedetection.svg)](https://github.com/azman0101/homelab/actions/workflows/changedetection.yml) | [changedetection](./changedetection) | Website change detection | v0.60.10 | — | `ghcr.io/azman0101/changedetection:v0.60.10@sha256:d8e46de6b1a263c8828fedcb8c046aa2c0219621f98c8b3db7df3c8b678d9f52` |

- **Built & Published badge**: latest workflow run across all branches and tags, including manual publications. Generated from the GitHub Actions API when a publication workflow starts or completes, with an hourly refresh. Green means success; red means failure; yellow means queued or running. Click a badge to open its workflow history.
- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
