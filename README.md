# Homelab Images

Signed, SBOM-attested, and Trivy-scanned container images for homelab use.

Every image in this repository is:
- 🔒 Built from **digest-pinned** upstream images
- 📋 Equipped with a **SBOM** (CycloneDX + SPDX)
- 🔏 **Signed** with Sigstore/Cosign (keyless, GitHub OIDC)
- 🛡️ **SLSA provenance** verified on every build
- 🔬 **Trivy-scanned** — results visible in the GitHub Security tab

## Images

Les PR modifiant la supply chain sont placées en **Draft sous embargo de 7 jours**,
sans build ni scan de leur contenu avant la levée.
Voir la [politique d'embargo](./docs/embargo.md).

| Built & Published | Image | Description | Published | Pending | Pull reference (`tag@digest`) |
|---|---|---|---|---|---|
| [![published](./.github/badges/home-assistant.svg)](https://github.com/azman0101/homelab/actions/workflows/home-assistant.yml) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.10.4 | — | `ghcr.io/azman0101/home-assistant:v2026.10.4@sha256:d4cc686a8933cc48182078aa797bbaac99daaa561c8175da07585be284e6b5ec` |
| [![published](./.github/badges/mosquitto.svg)](https://github.com/azman0101/homelab/actions/workflows/mosquitto.yml) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:77ec314b4ac08a13b44866e90354d34e79d8c131249a122b376bbdf41789e95d` |
| [![published](./.github/badges/frigate.svg)](https://github.com/azman0101/homelab/actions/workflows/frigate.yml) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:fbe6e3646ab2f4153b21d9a8efadab56915ff94749c8053063149b0ea89ac080` |
| [![published](./.github/badges/caddy.svg)](https://github.com/azman0101/homelab/actions/workflows/caddy.yml) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.7 | — | `ghcr.io/azman0101/caddy:v2.11.7@sha256:daf1f1df10c3a9833546c8d4138f8c870f5e37b7443a7d01af20b9b6a2e4731c` |
| [![published](./.github/badges/crowdsec.svg)](https://github.com/azman0101/homelab/actions/workflows/crowdsec.yml) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.1 | — | `ghcr.io/azman0101/crowdsec:v1.8.1@sha256:b3aa18932c306ab32d7e759337c737449f1153ea997902b97e47a8c8e0c71035` |
| [![published](./.github/badges/authelia.svg)](https://github.com/azman0101/homelab/actions/workflows/authelia.yml) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:004fff3db0921e0a8cc7b51bdf58cf73db2298cf979b4e4e2426ae3edb3faf89` |
| [![published](./.github/badges/redis.svg)](https://github.com/azman0101/homelab/actions/workflows/redis.yml) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:10b0e6a390555d24a0ab800aafffe25b1edb1da52e42b837813605eee8016731` |
| [![published](./.github/badges/postfix-relay.svg)](https://github.com/azman0101/homelab/actions/workflows/postfix-relay.yml) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:aea6904c8fdf0e4755f470ca99b4449737357a4175b4a620329707a2118fbf95` |
| [![published](./.github/badges/pihole.svg)](https://github.com/azman0101/homelab/actions/workflows/pihole.yml) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.10.0 | — | `ghcr.io/azman0101/pihole:v2026.10.0@sha256:9a6369a05503202d7ae18a8b6f83385ccfff5808ba796fb4dbd56a01598eda8b` |
| [![published](./.github/badges/uptime-kuma.svg)](https://github.com/azman0101/homelab/actions/workflows/uptime-kuma.yml) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.7 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.7@sha256:67b90397c7397e33db6832f6a6181738a0571147522a4fae43d584b00c27f5b3` |
| [![published](./.github/badges/influxdb.svg)](https://github.com/azman0101/homelab/actions/workflows/influxdb.yml) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:f41fdee0e5e857554de832457aa5b21a08b9c7fac5ae3e9cad65ec565c80d279` |
| [![published](./.github/badges/portainer-ce.svg)](https://github.com/azman0101/homelab/actions/workflows/portainer-ce.yml) | [portainer-ce](./portainer-ce) | Portainer Community Edition | v2.45.3 | — | `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:da1d3b9c07d489cdba712880ba07a95839e134374710023605c0053e8a20983e` |
| [![published](./.github/badges/changedetection.svg)](https://github.com/azman0101/homelab/actions/workflows/changedetection.yml) | [changedetection](./changedetection) | Website change detection | v0.60.10 | — | `ghcr.io/azman0101/changedetection:v0.60.10@sha256:0de5a9f0effd5e300f4aa14b679e9f7689acba979f4cb951344bcbca3064af5f` |

- **Built & Published badge**: latest workflow run across all branches and tags, including manual publications. Generated from the GitHub Actions API when a publication workflow starts or completes, with an hourly refresh. Green means success; red means failure; yellow means queued or running. Click a badge to open its workflow history.
- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
