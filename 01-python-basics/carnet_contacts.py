"""
Carnet de Contacts - Application console en Python
Fonctionnalités : ajouter, afficher, rechercher, modifier, supprimer,
trier et sauvegarder des contacts dans un fichier.

Chaque contact est un dictionnaire avec les clés : nom, telephone, email.
Tous les contacts sont stockés dans une liste, sauvegardée en JSON
dans le fichier contacts.txt.
"""

import json

# Liste globale qui contient tous les contacts (liste de dictionnaires)
contacts = []


def ajouter_contact():
    """Demande les infos d'un nouveau contact et l'ajoute à la liste,
    en évitant les doublons de nom."""
    nom = input("Nom : ")
    telephone = input("Téléphone : ")
    email = input("Email : ")

    # Vérifier si le nom existe déjà (comparaison insensible à la casse)
    for contact in contacts:
        if contact["nom"].lower() == nom.lower():
            print("Ce contact existe déjà !")
            return
    #reation du dictionnaire
    nouveau_contact = {
        "nom": nom,
        "telephone": telephone,
        "email": email
    }
   # ajout d'un contact dans la liste
    contacts.append(nouveau_contact)
    print(f"Contact '{nom}' ajouté avec succès !")


def afficher_contacts():
    """Affiche tous les contacts de la liste, numérotés."""
    if len(contacts) == 0:
        print("Aucun contact enregistré.")
        return

    print("--- Liste des contacts ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['nom']} | {contact['telephone']} | {contact['email']}")


def rechercher_contact():
    """Demande un nom et affiche tous les contacts dont le nom
    contient ce texte (recherche partielle, insensible à la casse)."""
    nom_recherche = input("Nom à rechercher : ")
    trouve = False

    for contact in contacts:
        if nom_recherche.lower() in contact["nom"].lower():
            print(f"{contact['nom']} | {contact['telephone']} | {contact['email']}")
            trouve = True

    if not trouve:
        print("Aucun contact trouvé.")


def supprimer_contact():
    """Demande un nom exact et supprime le contact correspondant."""
    nom_a_supprimer = input("Nom du contact à supprimer : ")

    for contact in contacts:
        if contact["nom"].lower() == nom_a_supprimer.lower():
            contacts.remove(contact)
            print(f"Contact '{contact['nom']}' supprimé avec succès !")
            return

    print("Contact introuvable.")


def modifier_contact():
    """Demande un nom exact et permet de modifier le téléphone
    et/ou l'email du contact correspondant."""
    nom_a_modifier = input("Nom du contact à modifier : ")

    for contact in contacts:
        if contact["nom"].lower() == nom_a_modifier.lower():
            print(f"Contact trouvé : {contact['nom']} | {contact['telephone']} | {contact['email']}")

            nouveau_telephone = input("Nouveau téléphone (laisse vide pour ne pas changer) : ")
            nouveau_email = input("Nouvel email (laisse vide pour ne pas changer) : ")

            if nouveau_telephone != "":
                contact["telephone"] = nouveau_telephone
            if nouveau_email != "":
                contact["email"] = nouveau_email

            print("Contact modifié avec succès !")
            return

    print("Contact introuvable.")


def trier_contacts():
    """Trie la liste des contacts par ordre alphabétique du nom."""
    contacts.sort(key=lambda contact: contact["nom"].lower())
    print("Contacts triés par ordre alphabétique !")


def sauvegarder_fichier():
    """Sauvegarde la liste des contacts dans contacts.txt au format JSON."""
    with open("contacts.txt", "w") as fichier:
        json.dump(contacts, fichier)
    print("Contacts sauvegardés avec succès !")


def charger_fichier():
    """Charge les contacts depuis contacts.txt au démarrage.
    Si le fichier n'existe pas encore, démarre avec une liste vide."""
    global contacts
    try:
        with open("contacts.txt", "r") as fichier:
            contacts = json.load(fichier)
        print("Contacts chargés avec succès !")
    except FileNotFoundError:
        contacts = []
        print("Aucun fichier trouvé, on démarre avec une liste vide.")


def menu():
    """Boucle principale : affiche le menu et exécute l'action choisie
    par l'utilisateur jusqu'à ce qu'il quitte le programme."""
    charger_fichier()

    while True:
        print("\n--- CARNET DE CONTACTS ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Modifier un contact")
        print("6. Trier les contacts")
        print("7. Sauvegarder les contacts")
        print("8. Quitter")

        choix = input("Choisis une option (1-8) : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            modifier_contact()
        elif choix == "6":
            trier_contacts()
        elif choix == "7":
            sauvegarder_fichier()
        elif choix == "8":
            sauvegarder_fichier()
            print("Au revoir !")
            break
        else:
            print("Option invalide, réessaie.")


if __name__ == "__main__":
    menu()
