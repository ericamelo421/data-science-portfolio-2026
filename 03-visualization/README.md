# Dashboard Visuel d'Exploration — World Happiness Report 2015

Ce projet transforme un ensemble de données en visualisations claires pour mieux 
comprendre les facteurs du bonheur dans le monde.

## Visualisations créées

- Distribution des variables clés (histogramme du score de bonheur)
- Corrélations entre variables (heatmap)
- Comparaisons par groupes (boxplot par région, bar chart top 10)
- Lien entre richesse et bonheur (scatter plot)
- Une visualisation interactive (Plotly — survol des pays par région)

## Insights clés

- Les 3 facteurs les plus liés au bonheur : PIB (0.78), Famille (0.74), Santé (0.72)
- La générosité est peu liée au bonheur (0.18) — résultat surprenant
- Western Europe domine, Sub-Saharan Africa en bas du classement
- La distribution mondiale du bonheur montre 2 groupes distincts

## Fichiers

- `data_visualization.ipynb` — notebook complet
- `01_top10_bonheur.png` à `05_histogramme_bonheur.png` — exports PNG
- `06_bonheur_interactif.html` — graphique Plotly interactif
- `2015.csv` — dataset World Happiness Report

## Technologies

Python, Pandas, Matplotlib, Seaborn, Plotly

