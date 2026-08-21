# Analyseur de Données CSV Personnel

Une application qui permet de calculer les statistiques d'un ensemble de données (moyenne, médiane, écart-type) et de détecter les valeurs aberrantes.

## Fonctionnalités

- Lecture d'un fichier CSV et extraction des valeurs numériques d'une colonne
- Calcul de statistiques de base (moyenne, médiane, min, max, écart-type)
- Détection des valeurs aberrantes
- Génération automatique d'un rapport texte, affiché et sauvegardé dans un fichier

## Utilisation

1. Place ton fichier CSV dans le même dossier que `csv_analyzer.py`
2. Ouvre `csv_analyzer.py` et modifie si besoin les variables `NOM_FICHIER` et `NOM_COLONNE` selon ton fichier
3. Lance le script :

```bash
python3 csv_analyzer.py
```

4. Le rapport s'affiche à l'écran et est sauvegardé dans `rapport.txt`

## Exemple de résultat

```
=== RAPPORT D'ANALYSE ===

Moyenne      : 13230.00
Médiane      : 5750.00
Minimum      : 500.00
Maximum      : 150000.00
Écart-type   : 32448.41

Valeurs aberrantes détectées (1) :
  - 150000.00
```