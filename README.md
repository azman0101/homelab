# Homelab Images

Signed, SBOM-attested, and Trivy-scanned container images for homelab use.

Every image in this repository is:
- 🔒 Built from **digest-pinned** upstream images
- 📋 Equipped with a **SBOM** (CycloneDX + SPDX)
- 🔏 **Signed** with Sigstore/Cosign (keyless, GitHub OIDC)
- 🛡️ **SLSA provenance** verified on every build
- 🔬 **Trivy-scanned** — results visible in the GitHub Security tab

## Images

Les PR modifiant la supply chain sont placées en **Draft sous embargo de 4 jours**,
sans build ni scan de leur contenu avant la levée.
Voir la [politique d'embargo](./docs/embargo.md).

| Built & Published | Image | Description | Published | Pending | Pull reference (`tag@digest`) |
|---|---|---|---|---|---|
| [![published](./.github/badges/home-assistant.svg)](https://github.com/azman0101/homelab/actions/workflows/home-assistant.yml) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.11.1 | — | `ghcr.io/azman0101/home-assistant:v2026.11.1@sha256:b01b6875ab389ddb91cca21bb51b6f81d874659b4cdc2c8ca8030b2d41ebc42a` |
| [![published](./.github/badges/mosquitto.svg)](https://github.com/azman0101/homelab/actions/workflows/mosquitto.yml) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:29fff708e9039db74211c1d03f083a1ded206f320bf6acc9ba68b3c735962981` |
| [![published](./.github/badges/frigate.svg)](https://github.com/azman0101/homelab/actions/workflows/frigate.yml) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:bec51a0bac9220616f384c192732a148c3a6bfe5544fb97befada09688d813ec` |
| [![published](./.github/badges/caddy.svg)](https://github.com/azman0101/homelab/actions/workflows/caddy.yml) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.7 | v2.11.9 | `ghcr.io/azman0101/caddy:v2.11.7@sha256:3efd4cf52b221bbaf750a0019f2f5a1c69e3e0f86c15b79891e96eab681971e8` |
| [![published](./.github/badges/crowdsec.svg)](https://github.com/azman0101/homelab/actions/workflows/crowdsec.yml) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.2 | — | `ghcr.io/azman0101/crowdsec:v1.8.2@sha256:cadfdfb1cdebceacb497b7db07879a2f71aa33fc65121c326997c14754014fef` |
| [![published](./.github/badges/authelia.svg)](https://github.com/azman0101/homelab/actions/workflows/authelia.yml) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:477b48f872981563fc6957bf656e5f33c9b0987ab1eb6c01e747498845178647` |
| [![published](./.github/badges/redis.svg)](https://github.com/azman0101/homelab/actions/workflows/redis.yml) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:e07cef791008382bf4e92436c5f0b66d3ff8ccdbc82c1432729b36a9082a4f14` |
| [![published](./.github/badges/postfix-relay.svg)](https://github.com/azman0101/homelab/actions/workflows/postfix-relay.yml) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:375e6d096445d2374d094e6c3b505df4e5ac3e474770fdd9c93df91d7ddd7e3c` |
| [![published](./.github/badges/pihole.svg)](https://github.com/azman0101/homelab/actions/workflows/pihole.yml) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.10.1 | — | `ghcr.io/azman0101/pihole:v2026.10.1@sha256:a248ce0da2b5384a46eb95922a0af33802225fad8cdfbd2ef96597e4d25c1818` |
| [![published](./.github/badges/uptime-kuma.svg)](https://github.com/azman0101/homelab/actions/workflows/uptime-kuma.yml) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.9 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.9@sha256:1b1cd785fa20eda8381f0a4fcda93ee1b6344d66f18d8a037368b31270b56f80` |
| [![published](./.github/badges/influxdb.svg)](https://github.com/azman0101/homelab/actions/workflows/influxdb.yml) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:3e77c2c0a38163ac5caf513b291078aca674b93215b108eb637f504e76898245` |
| [![published](./.github/badges/portainer-ce.svg)](https://github.com/azman0101/homelab/actions/workflows/portainer-ce.yml) | [portainer-ce](./portainer-ce) | Portainer Community Edition | v2.45.3 | — | `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:73435e5d784f73b7c48f97bc6cd8540fbb3f76e1a64f6eaf1d344f282fc6f83c` |
| [![published](./.github/badges/changedetection.svg)](https://github.com/azman0101/homelab/actions/workflows/changedetection.yml) | [changedetection](./changedetection) | Website change detection | v0.60.10 | v0.70.3 | `ghcr.io/azman0101/changedetection:v0.60.10@sha256:87ce5b102e7a678fcb7fa3f582a2acc5411c4b37de24e4cbef504592c0f1e9d9` |

- **Built & Published badge**: latest workflow run across all branches and tags, including manual publications. Generated from the GitHub Actions API when a publication workflow starts or completes, with an hourly refresh. Green means success; red means failure; yellow means queued or running. Click a badge to open its workflow history.
- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
