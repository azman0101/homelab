# Embargo des mises à jour de supply chain

La politique est configurée dans [`.github/embargo.json`](../.github/embargo.json).
Le contrôleur et sa configuration restent dans `homelab`. Aucun service externe
n'est nécessaire pour cette première version.

## Parcours d'une PR

1. La PR est ouverte immédiatement : Dependabot ne retarde pas sa création.
2. Le contrôleur observe son SHA, enregistre l'heure de première observation dans
   un commentaire signé par `github-actions[bot]`, pose le label
   **supply-chain: embargo**, et convertit la PR en **Draft**.
3. Pendant **7 jours**, le statut **Supply chain embargo** reste en attente.
   Aucun checkout du contenu de la PR, build, test de conteneur ou scan Trivy de
   cette PR n'est lancé par les workflows de validation.
4. Chaque nouveau commit remet le délai à zéro, même pour une modification mineure.
   Le calcul ignore les dates de commit et de publication fournies par l'amont.
5. Un contrôle horaire lève l'embargo au plus tôt à l'échéance, remplace le label
   par **supply-chain: eligible**, et remet la PR en Ready si le contrôleur l'avait
   lui-même mise en Draft. Une PR initialement ouverte en Draft reste en Draft
   jusqu'à une action de son auteur.
6. Le contrôleur déclenche explicitement la validation de ce SHA. Le workflow
   vérifie à nouveau l'état de l'embargo avant tout checkout de contenu candidat.
   La PR n'est pas fusionnée automatiquement.

Un retrait du label ou un passage manuel en Ready ne constitue pas une levée.
La prochaine réconciliation remet la PR sous embargo. Une nouvelle exécution
manuelle de `Validate Images PR` ne permet pas d'ignorer le délai.

La portée inclut tous les fichiers sauf README, documentation, licences et badges
générés. Elle couvre donc Dockerfiles, fichiers ajoutés aux contextes de build,
GitHub Actions, scripts, tests et fichiers de dépendances, quelle que soit la
personne ou le bot qui ouvre la PR. Les chemins exclus sont configurables.

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
- Le statut **Supply chain embargo** doit être requis par la règle de protection
  de la branche par défaut, sinon un mainteneur pourrait passer manuellement une
  PR en Ready et la fusionner avant la réconciliation.
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
