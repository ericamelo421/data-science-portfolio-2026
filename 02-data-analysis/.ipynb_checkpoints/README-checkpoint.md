# Tableau de Bord d'Analyse de Ventes

Ce projet analyse les ventes d'une entreprise (dataset Superstore) : ventes par région, catégorie et mois, top 10 des produits, et rentabilité par segment client. Les résultats sont exportés automatiquement dans un fichier Excel à plusieurs feuilles.

## Fonctionnalités

- Chargement et vérification du dataset (9994 ventes, aucune valeur manquante)
- Analyse des ventes par région, catégorie et mois
- Identification du top 10 des produits les plus vendus
- Analyse de la rentabilité par segment client (en total ET par client, pour éviter les conclusions trompeuses)
- Fusion avec un tableau de correspondance région/manager
- Export automatique des résultats en Excel multi-feuilles

## Utilisation

1. Place le fichier `Sample - Superstore.csv` dans le même dossier que le notebook
2. Exécute les cellules du notebook dans l'ordre
3. Le fichier `rapport_ventes.xlsx` est généré automatiquement, avec 3 feuilles (Ventes par région, Top 10 produits, Profit par segment)

## Insights clés

- 9994 lignes de vente correspondent en réalité à seulement 5009 commandes et 793 clients uniques (un client passe en moyenne 6,3 commandes)
- 18,7% des ventes sont réalisées à perte (Profit négatif), souvent liées aux fortes remises
- En profit total, le segment Consumer domine (134 119) — mais en profit **par client**, c'est Home Office qui est le plus rentable (407 vs 328 pour Consumer). Un total élevé peut simplement refléter un plus grand nombre de clients, pas une meilleure rentabilité individuelle
- Novembre et Décembre sont les mois les plus actifs, cohérent avec le Black Friday et les fêtes de fin d'année

## Exemple de résultat

```
Top 3 des ventes par région :
West       725457.82
East       678781.24
Central    501239.89

Profit moyen par client, par segment :
Home Office    407.42
Corporate      389.74
Consumer       327.92
```