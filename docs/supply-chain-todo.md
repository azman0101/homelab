# Supply chain : pistes en attente d'arbitrage

Revue d'une proposition de « gatekeeper » supply chain (novembre 2026). Rien n'est
implémenté ici ; chaque point attend une décision.

## À faire sans arbitrage particulier

- [ ] Épingler par SHA `github/codeql-action/upload-sarif@v4` dans
      `.github/workflows/trivy-pr.yml` (seule action encore référencée par tag).

## Choix à arbitrer

- [ ] **Gate OSV `MAL-*` sur l'image candidate.** `osv-scanner` sur l'image
      construite par `validate-image.yml` après l'embargo ; échec uniquement sur les
      identifiants `MAL-*`. Couvre les paquets de langage (npm, PyPI, modules Go,
      crates…), pas apk/deb. *À décider : bloquant ou informatif ; versions d'outil.*
- [ ] **Rescan hebdomadaire des images publiées sur GHCR.** Les entrées `MAL-*`
      arrivent souvent après la publication : c'est la vraie lacune, l'embargo ne
      protège qu'à l'entrée. *À décider : canal d'alerte (issue, notification),
      action en cas de détection (retrait du tag `latest` ?).*
- [ ] **Diff de configuration entre ancien et nouveau digest** (ENTRYPOINT, CMD,
      USER, ports, env, nouveaux binaires setuid), publié en commentaire de PR.
      *À décider : informatif seulement, ou bloquant sur certains champs.*
- [ ] **Vérification des mises à jour de digest des images officielles Docker**
      (caddy, redis, influxdb, eclipse-mosquitto) contre
      `docker-library/official-images` ou `docker-library/repo-info`, pour repérer un
      tag réécrit. *À vérifier d'abord : délai de mise à jour de ces sources.*
- [ ] **Délai d'embargo.** Réduit à 4 jours. *À réévaluer avec l'expérience ;
      la statistique « 90 % détectés sous 72 h » n'est pas sourcée.*

## Écartés (sauf nouvel élément)

- **Signatures cosign / attestations SLSA des images amont** : vérifié le
  2026-11-06, 0 image sur 13 avec une signature cosign (format `.sig`/`.att`) ; les
  13 publient des attestations BuildKit non signées, falsifiables par quiconque a
  le jeton de publication. Non vérifié : API d'attestations GitHub, référents OCI.
- **capslock** : nécessite les sources Go et l'arbre de modules (faisable seulement
  pour caddy, compilé ici) ; bruyant sur les versions mineures.
- **Recherche de mots-clés dans les issues amont comme gate** : faux positifs
  (CrowdSec est un produit de sécurité) et abus possible (n'importe qui peut ouvrir
  une issue pour bloquer une mise à jour). Au mieux en commentaire informatif.
- **Âge calculé depuis la date de release amont** : falsifiable par un tag
  détourné vers une ancienne release. Le contrôleur compte depuis sa propre
  première observation, ce qu'il faut conserver.
