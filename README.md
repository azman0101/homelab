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
| [![published](./.github/badges/mosquitto.svg)](https://github.com/azman0101/homelab/actions/workflows/mosquitto.yml) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:77ec314b4ac08a13b44866e90354d34e79d8c131249a122b376bbdf41789e95d` |
| [![published](./.github/badges/frigate.svg)](https://github.com/azman0101/homelab/actions/workflows/frigate.yml) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.2 | — | `ghcr.io/azman0101/frigate:v0.18.2@sha256:bec51a0bac9220616f384c192732a148c3a6bfe5544fb97befada09688d813ec` |
| [![published](./.github/badges/caddy.svg)](https://github.com/azman0101/homelab/actions/workflows/caddy.yml) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.7 | — | `ghcr.io/azman0101/caddy:v2.11.7@sha256:59a8f277dd087006e40aa43d28f89c3dee557f3e91f96e19ffc770f5c3af2f23` |
| [![published](./.github/badges/crowdsec.svg)](https://github.com/azman0101/homelab/actions/workflows/crowdsec.yml) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.2 | — | `ghcr.io/azman0101/crowdsec:v1.8.2@sha256:23bda8c444d0c5341735ac97ee22d11b303d44c3fd1159d3217dda09c313dc35` |
| [![published](./.github/badges/authelia.svg)](https://github.com/azman0101/homelab/actions/workflows/authelia.yml) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:d163305769b7e36438276f3f47a5cb98e3c9015af5af4433b9aa236ff3c52b47` |
| [![published](./.github/badges/redis.svg)](https://github.com/azman0101/homelab/actions/workflows/redis.yml) | [redis](./redis) | Redis in-memory data store | v8.10.2-alpine | — | `ghcr.io/azman0101/redis:v8.10.2-alpine@sha256:86528afeb8f418923700eea4aee49a015f2169f8e7bad0af6f2f4979ab051469` |
| [![published](./.github/badges/postfix-relay.svg)](https://github.com/azman0101/homelab/actions/workflows/postfix-relay.yml) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:aea6904c8fdf0e4755f470ca99b4449737357a4175b4a620329707a2118fbf95` |
| [![published](./.github/badges/pihole.svg)](https://github.com/azman0101/homelab/actions/workflows/pihole.yml) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.10.1 | — | `ghcr.io/azman0101/pihole:v2026.10.1@sha256:a248ce0da2b5384a46eb95922a0af33802225fad8cdfbd2ef96597e4d25c1818` |
| [![published](./.github/badges/uptime-kuma.svg)](https://github.com/azman0101/homelab/actions/workflows/uptime-kuma.yml) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.9 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.9@sha256:a4185d225469193818a79457db4abff255ced93d10a16d1f191f278e38d1e6ec` |
| [![published](./.github/badges/influxdb.svg)](https://github.com/azman0101/homelab/actions/workflows/influxdb.yml) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:f41fdee0e5e857554de832457aa5b21a08b9c7fac5ae3e9cad65ec565c80d279` |
| [![published](./.github/badges/portainer-ce.svg)](https://github.com/azman0101/homelab/actions/workflows/portainer-ce.yml) | [portainer-ce](./portainer-ce) | Portainer Community Edition | v2.45.3 | — | `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:722c678d5754d5d69132d95fc2751cd9499241fcefe2977d6ddec6991e2a0fe6` |
| [![published](./.github/badges/changedetection.svg)](https://github.com/azman0101/homelab/actions/workflows/changedetection.yml) | [changedetection](./changedetection) | Website change detection | v0.60.10 | — | `ghcr.io/azman0101/changedetection:v0.60.10@sha256:231d9dcb0ee63dc90ad6f14efd0e48fe18b94e22096558d8eed0004c21dd2c6e` |

- **Built & Published badge**: latest workflow run across all branches and tags, including manual publications. Generated from the GitHub Actions API when a publication workflow starts or completes, with an hourly refresh. Green means success; red means failure; yellow means queued or running. Click a badge to open its workflow history.
- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
