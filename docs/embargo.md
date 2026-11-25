# Embargo des mises à jour de supply chain

La politique est configurée dans [`.github/embargo.json`](../.github/embargo.json).
Le contrôleur et sa configuration restent dans `homelab`. Aucun service externe
n'est nécessaire pour cette première version.

## Parcours d'une PR

1. Dependabot vérifie les mises à jour de version chaque jour. Le cooldown natif
   rend les nouvelles versions éligibles après 4 jours. Dès son ouverture,
   la PR entre dans l’embargo local de 4 jours.
2. Le contrôleur observe son SHA, enregistre l'heure de première observation dans
   un commentaire signé par `github-actions[bot]`, pose le label
   **supply-chain: embargo** et bloque la fusion par le statut requis. La gestion
   automatique des Draft est désactivée (`manage_drafts: false`), car le jeton
   du contrôleur ne dispose pas de cette capacité. Aucun appel de conversion
   en Draft ou de passage en Ready n'est donc effectué.
3. Pendant **4 jours**, le statut **Supply chain embargo** reste en attente.
   Aucun checkout du contenu de la PR, build, test de conteneur ou scan Trivy de
   cette PR n'est lancé par les workflows de validation.
4. Chaque nouveau commit qui modifie le contenu remet le délai à zéro, même pour une
   modification mineure. Un commit qui porte exactement les mêmes changements (rebase
   de Dependabot sur `main`) conserve le temps déjà écoulé : l'identité du changement
   est l'empreinte des fichiers modifiés (chemin, statut et blob Git de chaque fichier
   sur la tête de la PR), pas le SHA du commit. La levée et la validation, elles,
   restent attachées au commit exact et sont refaites pour le nouveau SHA.
   Le calcul ignore les dates de commit et de publication fournies par l'amont.
5. Un contrôle planifié (deux fois par heure) lève l'embargo au plus tôt à l'échéance, remplace le label
   par **supply-chain: eligible**. Une PR en Draft reste en Draft jusqu'à une
   action de son auteur ; sa validation attend ce passage manuel en Ready.
6. Le contrôleur déclenche explicitement la validation de ce SHA. Le workflow
   vérifie à nouveau l'état de l'embargo avant tout checkout de contenu candidat,
   puis publie son résultat dans le statut **Validate images** de ce SHA. Une
   validation restée en attente plus de 3 heures (annulée, perdue) est relancée
   par le contrôleur ; un échec réel n'est pas relancé automatiquement.
   La PR n'est pas fusionnée automatiquement.

Aucune relance manuelle n'est nécessaire pour lever l'embargo : les statuts sont
mis à jour sur le SHA de la PR par chaque réconciliation.

Un retrait du label ou un passage manuel en Ready ne constitue pas une levée.
La prochaine réconciliation remet la PR sous embargo. Une nouvelle exécution
manuelle de `Validate Images PR` ne permet pas d'ignorer le délai.

La portée inclut tous les fichiers sauf README, documentation, licences et badges
générés. Une PR qui ne touche que ces fichiers n'est pas mise sous embargo et reçoit
directement les deux statuts requis en succès, puisqu'aucune image n'est à valider. Elle couvre donc Dockerfiles, fichiers ajoutés aux contextes de build,
GitHub Actions, scripts, tests et fichiers de dépendances, quelle que soit la
personne ou le bot qui ouvre la PR. Les chemins exclus sont configurables.

## Cooldown Dependabot

La configuration de [Dependabot](../.github/dependabot.yml) applique
`schedule.interval: daily`, `cooldown.default-days: 4` et
`rebase-strategy: disabled` à chaque entrée Docker et GitHub Actions.

Le cooldown natif est calculé depuis la publication de la version. Plusieurs
versions devenues éligibles peuvent donner lieu à des PR le même jour, et une
nouvelle version éligible peut remplacer une PR existante. Un recalcul peut
également fermer une PR si sa version est encore dans le cooldown.

L’embargo local dure 4 jours à partir de la première observation du changement
dans la PR. La durée configurée sur `main` s’applique aussi aux PR déjà en attente.
Un rebase manuel qui conserve le même contenu préserve le délai déjà écoulé.

Les mises à jour de sécurité restent soumises à l’embargo local. Elles suivent
leur propre cadence et sont exemptées du cooldown natif.

Référence : [options Dependabot](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).

## Gestion optionnelle des Draft

`manage_drafts: false` désactive tous les changements automatiques de Draft/Ready.
Cette option est indépendante des 4 jours d'embargo et des statuts requis.

Si la gestion des Draft est réactivée avec un jeton adapté, le premier refus
`FORBIDDEN` (GraphQL ou HTTP 403) est mémorisé dans l'état signé de la PR avec
`draft_forbidden: true`. Le contrôleur ne retente plus aucune mutation Draft/Ready
pour cette PR, même après un nouveau commit. L'avertissement n'est émis qu'au
premier refus enregistré. Les autres erreurs ne sont pas masquées comme des
refus de permission. Une réactivation après correction des droits nécessite
une remise à zéro explicite de cet état par un mainteneur.

## Fonctionnement et permissions

- `pr-embargo.yml` utilise `pull_request_target`, la planification et un lancement
  manuel. Il exécute uniquement le contrôleur de la branche par défaut, jamais le
  code de la PR, et ne télécharge aucun artefact provenant de celle-ci.
- Le contrôleur a les droits nécessaires pour gérer Draft, labels, commentaire,
  statut et déclenchement de validation. Les jobs exécutant le contenu de la PR
  disposent uniquement de droits de lecture et ne reçoivent pas de secrets de
  publication. Les identifiants de checkout ne sont pas conservés.
- Le délai est vérifié par SHA, pas par label. Les commentaires écrits par les
  auteurs de PR sont ignorés. Les PR dépassant la limite de 3 000 fichiers de
  l'API GitHub restent bloquées pour examen.
- Les statuts **Supply chain embargo** et **Validate images** doivent être requis
  par la règle de protection de la branche par défaut. Sans eux, rien n'empêche
  de fusionner une PR sous embargo ou dont la validation a échoué : la conversion
  en Draft n'est qu'un confort et n'est pas garantie.
- Ne pas ajouter de nouveau workflow `pull_request` exécutant du contenu candidat
  sans passer par ce contrôleur. Le dispositif protège les workflows gérés ici ;
  il ne remplace pas les politiques GitHub d'approbation des workflows de forks.

Une planification GitHub Actions peut être retardée ; cela prolonge l'attente,
sans rendre une PR éligible prématurément. Le contrôleur peut aussi être lancé
manuellement. Si une opération échoue, l'état reste bloquant et le workflow
signale l'erreur.

## Limites de cette première version

L'embargo n'est pas une preuve d'innocuité. La surveillance des compromissions,
retraits de tags et images déjà publiées sera ajoutée séparément. Les constructions
de `main` et des tags déjà publiés continuent de fonctionner ; la quarantaine
concerne l'introduction de changements via les PR.

## Vérifications locales

```sh
python3 -m unittest discover -s scripts/tests -v
```

Ces tests n'exécutent aucun conteneur et simulent toutes les interactions GitHub.
