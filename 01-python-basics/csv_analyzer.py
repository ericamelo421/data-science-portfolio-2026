"""
Analyseur de Données CSV Personnel
Lit un fichier CSV, calcule des statistiques de base, détecte les valeurs
aberrantes, et génère un rapport texte automatique.

Usage : modifie NOM_FICHIER et NOM_COLONNE ci-dessous selon ton fichier.
"""

import csv
import statistics

NOM_FICHIER = "depenses.csv"
NOM_COLONNE = "montant"  # la colonne numérique à analyser


def lire_csv(nom_fichier, nom_colonne):
    """Lit le fichier CSV et renvoie la liste des valeurs numériques
    de la colonne demandée."""
    valeurs = []

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            try:
                valeurs.append(float(ligne[nom_colonne]))
            except ValueError:
                print(f"Valeur ignorée (non numérique) : {ligne[nom_colonne]}")

    return valeurs


def calculer_statistiques(valeurs):
    """Calcule moyenne, médiane, min et max, et renvoie le tout
    dans un dictionnaire."""
    return {
        "moyenne": statistics.mean(valeurs),
        "mediane": statistics.median(valeurs),
        "min": min(valeurs),
        "max": max(valeurs),
        "ecart_type": statistics.stdev(valeurs)
    }


def trouver_valeurs_aberrantes(valeurs, stats):
    """Considère comme aberrante toute valeur trop éloignée de la
    moyenne (plus de 2 écarts-types), une méthode simple et courante."""
    seuil_bas = stats["moyenne"] - 2 * stats["ecart_type"]
    seuil_haut = stats["moyenne"] + 2 * stats["ecart_type"]

    aberrantes = [v for v in valeurs if v < seuil_bas or v > seuil_haut]
    return aberrantes


def generer_rapport(stats, aberrantes, nom_fichier_sortie="rapport.txt"):
    """Écrit un rapport texte lisible avec les résultats de l'analyse."""
    lignes = []
    lignes.append("=== RAPPORT D'ANALYSE ===\n")
    lignes.append(f"Moyenne      : {stats['moyenne']:.2f}")
    lignes.append(f"Médiane      : {stats['mediane']:.2f}")
    lignes.append(f"Minimum      : {stats['min']:.2f}")
    lignes.append(f"Maximum      : {stats['max']:.2f}")
    lignes.append(f"Écart-type   : {stats['ecart_type']:.2f}\n")

    if aberrantes:
        lignes.append(f"Valeurs aberrantes détectées ({len(aberrantes)}) :")
        for v in aberrantes:
            lignes.append(f"  - {v:.2f}")
    else:
        lignes.append("Aucune valeur aberrante détectée.")

    contenu = "\n".join(lignes)

    with open(nom_fichier_sortie, "w", encoding="utf-8") as fichier:
        fichier.write(contenu)

    print(contenu)
    print(f"\nRapport sauvegardé dans {nom_fichier_sortie}")


if __name__ == "__main__":
    valeurs = lire_csv(NOM_FICHIER, NOM_COLONNE)
    stats = calculer_statistiques(valeurs)
    aberrantes = trouver_valeurs_aberrantes(valeurs, stats)
    generer_rapport(stats, aberrantes)
