# Embargo des mises à jour de supply chain

La politique est configurée dans [`.github/embargo.json`](../.github/embargo.json).
Le contrôleur et sa configuration restent dans `homelab`. Aucun service externe
n'est nécessaire pour cette première version.

## Parcours d'une PR

1. Dependabot propose les mises à jour de version par lots les **1er et 15 de chaque
   mois à 06:00 UTC**, après un cooldown de **7 jours** lorsque la date de
   publication est disponible. Dès son ouverture, la PR entre dans l’embargo.
2. Le contrôleur observe son SHA, enregistre l'heure de première observation dans
   un commentaire signé par `github-actions[bot]`, pose le label
   **supply-chain: embargo**, et tente de convertir la PR en **Draft**. Si GitHub
   refuse cette conversion au jeton du workflow, un avertissement est émis et
   l'embargo reste porté par le statut requis : le contrôleur ne passe pas en échec.
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

## Cooldown et fenêtre de fusion Dependabot

La configuration de [Dependabot](../.github/dependabot.yml) applique aux
13 images Docker et aux GitHub Actions :

- `cooldown.default-days: 7` : une nouvelle version doit avoir au moins 7 jours
  avant d'être proposée, lorsque son âge est connu du registre ;
- `schedule.interval: cron`, `cronjob: "0 6 1,15 * *"` : deux campagnes par mois,
  espacées de 14 à 17 jours, plutôt qu'une vérification quotidienne susceptible
  de remplacer les PR par une nouvelle version ;
- `rebase-strategy: disabled` : pas de rebase automatique des nouvelles PR lorsque
  `main` évolue. Si un conflit exige un rebase, il doit être demandé explicitement
  et le nouveau SHA recommence son embargo.

Exemple : une PR ouverte le 1er devient éligible au plus tôt le 8, ce qui laisse
ensuite environ 7 jours pour la valider et la fusionner avant la campagne du 15.
Le contrôleur horaire et la durée de validation peuvent réduire cette fenêtre.
Le cooldown et l'embargo sont deux délais distincts ; le cooldown ne remplace
jamais l'observation locale du SHA pendant 7 jours avant de l'exécuter.

Un cooldown seul ne fige pas une PR existante. Pour Docker, les dates de
publication peuvent aussi être absentes, notamment pour un changement de digest
sans changement de tag. La cadence espacée reste donc importante même lorsque
Dependabot ne peut pas appliquer le cooldown natif.

Les mises à jour de sécurité ne suivent pas le cooldown ni le calendrier des
mises à jour de version ; elles peuvent donc interrompre cette cadence. Elles
restent soumises à l'embargo du dépôt : cette configuration n'autorise aucun
build anticipé. Un lancement manuel de Dependabot peut également créer une PR
en dehors des deux campagnes.

GitHub indique que les PR déjà ouvertes lors de la désactivation des rebases
peuvent continuer à être rebasées jusqu'à 30 jours après leur ouverture. Cette
configuration ne promet donc pas de figer immédiatement les PR existantes, ni de
conserver indéfiniment une PR non fusionnée au-delà de la campagne suivante.

Référence : [options Dependabot : cooldown, rebase et calendrier](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).

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
