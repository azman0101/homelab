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
| [![published](./.github/badges/home-assistant.svg)](https://github.com/azman0101/homelab/actions/workflows/home-assistant.yml) | [home-assistant](./home-assistant) | Home Assistant - Open source home automation | v2026.11.3 | — | `ghcr.io/azman0101/home-assistant:v2026.11.3@sha256:a5ce9566a2646a0dce73f3dd620e87913de78d19fa4af0b573493441c47c656a` |
| [![published](./.github/badges/mosquitto.svg)](https://github.com/azman0101/homelab/actions/workflows/mosquitto.yml) | [mosquitto](./mosquitto) | Eclipse Mosquitto MQTT broker | v2.1.2-alpine | — | `ghcr.io/azman0101/mosquitto:v2.1.2-alpine@sha256:699e731db4f97b905add42a04db1ff85fb40c663033e2725f3159147aacd0597` |
| [![published](./.github/badges/frigate.svg)](https://github.com/azman0101/homelab/actions/workflows/frigate.yml) | [frigate](./frigate) | Frigate NVR - Network Video Recorder with local AI object detection | v0.18.3 | — | `ghcr.io/azman0101/frigate:v0.18.3@sha256:128f2c86533b5e371a6cb3a8e2d819c901eeeeaac2892680ce6f5ccaa44a7567` |
| [![published](./.github/badges/caddy.svg)](https://github.com/azman0101/homelab/actions/workflows/caddy.yml) | [caddy](./caddy) | Caddy web server with CrowdSec bouncer | v2.11.9 | — | `ghcr.io/azman0101/caddy:v2.11.9@sha256:585fc5a14a1f49ae0bf1fd9c778bfd742e1e5422a66d99edea55d8d325a07032` |
| [![published](./.github/badges/crowdsec.svg)](https://github.com/azman0101/homelab/actions/workflows/crowdsec.yml) | [crowdsec](./crowdsec) | CrowdSec - collaborative security engine | v1.8.2 | — | `ghcr.io/azman0101/crowdsec:v1.8.2@sha256:0368149515efb042efacfa9bc2fd5afc490fd0a8e9c2e4f35e842a5197c2cffe` |
| [![published](./.github/badges/authelia.svg)](https://github.com/azman0101/homelab/actions/workflows/authelia.yml) | [authelia](./authelia) | Authelia - open-source authentication and authorization server | v4.39.28 | — | `ghcr.io/azman0101/authelia:v4.39.28@sha256:d43c51f1dd822e5c7a25983adddf8bd4b0c60d10ddaccb133faa08bead6ec673` |
| [![published](./.github/badges/redis.svg)](https://github.com/azman0101/homelab/actions/workflows/redis.yml) | [redis](./redis) | Redis in-memory data store | v8.10.3-alpine | — | `ghcr.io/azman0101/redis:v8.10.3-alpine@sha256:020d8f83c45e2fb11f8bba05d606132371d14d4d3c9f04798ea22cab318e8044` |
| [![published](./.github/badges/postfix-relay.svg)](https://github.com/azman0101/homelab/actions/workflows/postfix-relay.yml) | [postfix-relay](./postfix-relay) | Postfix relay - lightweight mail relay | v1.2.17 | — | `ghcr.io/azman0101/postfix-relay:v1.2.17@sha256:8702ee066fc399acb06e13a77ad34c2ab92f658f7fec5179f726cb5c1004cc72` |
| [![published](./.github/badges/pihole.svg)](https://github.com/azman0101/homelab/actions/workflows/pihole.yml) | [pihole](./pihole) | Pi-hole - network-wide ad blocking | v2026.11.0 | — | `ghcr.io/azman0101/pihole:v2026.11.0@sha256:43c269940f27c320d9233389e0459e260a5f02380e15381cda8abfb528122b5a` |
| [![published](./.github/badges/uptime-kuma.svg)](https://github.com/azman0101/homelab/actions/workflows/uptime-kuma.yml) | [uptime-kuma](./uptime-kuma) | Uptime Kuma - Self-hosted monitoring tool | v2.5.9 | — | `ghcr.io/azman0101/uptime-kuma:v2.5.9@sha256:cc98f709c52bebe41f65184980a59ee81bc25d08b92748e904cdf96b14ee4cd2` |
| [![published](./.github/badges/influxdb.svg)](https://github.com/azman0101/homelab/actions/workflows/influxdb.yml) | [influxdb](./influxdb) | InfluxDB - Open-source time-series database | v2.9.1-alpine | — | `ghcr.io/azman0101/influxdb:v2.9.1-alpine@sha256:d7afc63836bdbd5f9d2cd17b4feede80743dde7e04ca0d74febfb102c5d610d7` |
| [![published](./.github/badges/portainer-ce.svg)](https://github.com/azman0101/homelab/actions/workflows/portainer-ce.yml) | [portainer-ce](./portainer-ce) | Portainer Community Edition | v2.45.3 | — | `ghcr.io/azman0101/portainer-ce:v2.45.3@sha256:032fb1861dede5bcf044a68cc94071120a72aaa0b3d3030d54fb914870ee3b33` |
| [![published](./.github/badges/changedetection.svg)](https://github.com/azman0101/homelab/actions/workflows/changedetection.yml) | [changedetection](./changedetection) | Website change detection | v0.70.3 | — | `ghcr.io/azman0101/changedetection:v0.70.3@sha256:7cc2b520740c223c585493e94390083846def9b4ee25bb7a9ac050ff1d4c44df` |

- **Built & Published badge**: latest workflow run across all branches and tags, including manual publications. Generated from the GitHub Actions API when a publication workflow starts or completes, with an hourly refresh. Green means success; red means failure; yellow means queued or running. Click a badge to open its workflow history.
- **Published**: tag currently pushed to GHCR. **Pending**: version declared in the Dockerfile but not built yet (`—` when up to date).
- **Pull reference**: copy-paste address (`tag` + `digest`) of the published image. These columns are maintained by the workflows, don't edit them by hand.

## Quick verify any image

```bash
cosign verify ghcr.io/<owner>/<image>:latest \
  --certificate-identity-regexp="https://github.com/<owner>/homelab" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```
