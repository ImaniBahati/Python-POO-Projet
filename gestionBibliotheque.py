from datetime import datetime, timedelta

class Auteur:
    def __init__(self, nom, nationalite):
        self.nom = nom
        self.nationalite = nationalite

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.emprunteur = None

    def emprunter(self, emprunteur):
        if self.emprunteur is None:
            nouvel_emprunt = Emprunt(self, emprunteur)
            self.emprunteur = emprunteur
            return nouvel_emprunt
        else:
            return "Ce livre est déjà emprunté par : " + self.emprunteur.nom

    def retourner(self):
        if self.emprunteur is not None:
            self.emprunteur = None
            return "Livre retourné avec succès"
        else:
            return "Ce livre n'est pas actuellement emprunté"

class Emprunteur:
    def __init__(self, nom, prenom, email):
        self.nom = nom
        self.prenom = prenom
        self.email = email

class Emprunt:
    def __init__(self, livre, emprunteur):
        self.livre = livre
        self.emprunteur = emprunteur
        self.date_emprunt = datetime.now()
        self.date_retour_limite = self.date_emprunt + timedelta(days=14)

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.auteurs = []
        self.emprunteurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def ajouter_auteur(self, auteur):
        self.auteurs.append(auteur)

    def ajouter_emprunteur(self, emprunteur):
        self.emprunteurs.append(emprunteur)

    def rechercher_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                return livre
        return None

    def rechercher_livre_par_auteur(self, auteur):
        livres_auteur = []
        for livre in self.livres:
            if livre.auteur == auteur:
                livres_auteur.append(livre)
        return livres_auteur

    def gerer_bibliotheque(self):
        while True:
            choix = input("Que souhaitez-vous faire ?\n" +
                          "1. Ajouter un livre\n" +
                          "2. Ajouter un auteur\n" +
                          "3. Ajouter un emprunteur\n" +
                          "4. Rechercher un livre par titre\n" +
                          "5. Rechercher un livre par auteur\n" +
                          "6. Emprunter un livre\n" +
                          "7. Retourner un livre\n" +
                          "8. Quitter\n")

            if choix == "1":
                titre = input("Entrez le titre du livre : ").upper()
                nom_auteur = input("Entrez le nom de l'auteur : ")
                nationalite_auteur = input("Entrez la nationalité de l'auteur : ")
                isbn = input("Entrez l'ISBN du livre : ")

                auteur = Auteur(nom_auteur, nationalite_auteur)
                livre = Livre(titre, auteur, isbn)

                self.ajouter_livre(livre)
                self.ajouter_auteur(auteur)
                print("Livre ajouté avec succès !")

            elif choix == "2":
                nom_auteur = input("Entrez le nom de l'auteur : ")
                nationalite_auteur = input("Entrez la nationalité de l'auteur : ")
                auteur = Auteur(nom_auteur, nationalite_auteur)
                self.ajouter_auteur(auteur)
                print("Auteur ajouté avec succès !")

            elif choix == "3":
                nom_emprunteur = input("Entrez le nom de l'emprunteur : ")
                prenom_emprunteur = input("Entrez le prénom de l'emprunteur : ")
                email_emprunteur = input("Entrez l'email de l'emprunteur : ")
                emprunteur = Emprunteur(nom_emprunteur, prenom_emprunteur, email_emprunteur)
                self.ajouter_emprunteur(emprunteur)
                print("Emprunteur ajouté avec succès !")
                
            elif choix == "4":
                titre_recherche = input("Entrez le titre du livre à rechercher : ").upper()
                livre_trouve = self.rechercher_livre_par_titre(titre_recherche)
                if livre_trouve:
                    print(f"Livre trouvé : {livre_trouve.titre} - {livre_trouve.auteur.nom}")
                else:
                    print(f"Aucun livre trouvé avec le titre '{titre_recherche}'")

            elif choix == "5":
                nom_auteur_recherche = input("Entrez le nom de l'auteur à rechercher : ")
                livres_auteur = self.rechercher_livre_par_auteur(nom_auteur_recherche)
                if livres_auteur:
                    print(f"Livres trouvés par {nom_auteur_recherche} :")
                    for livre in livres_auteur:
                        print(f"- {livre.titre}")
                else:
                    print(f"Aucun livre trouvé pour l'auteur '{nom_auteur_recherche}'")

            elif choix == "6":
                titre_emprunt = input("Entrez le titre du livre à emprunter : ")
                livre_a_emprunter = self.rechercher_livre_par_titre(titre_emprunt)
                if livre_a_emprunter:
                    nom_emprunteur = input("Entrez le nom de l'emprunteur : ")
                    emprunteur_trouve = None
                    for emprunteur in self.emprunteurs:
                        if emprunteur.nom == nom_emprunteur:
                            emprunteur_trouve = emprunteur
                            break
                    if emprunteur_trouve:
                        resultat_emprunt = livre_a_emprunter.emprunter(emprunteur_trouve)
                        print(resultat_emprunt)
                    else:
                        print(f"Aucun emprunteur trouvé avec le nom '{nom_emprunteur}'")
                else:
                    print(f"Aucun livre trouvé avec le titre '{titre_emprunt}'")

            elif choix == "7":
                titre_retour = input("Entrez le titre du livre à retourner : ")
                livre_a_retourner = self.rechercher_livre_par_titre(titre_retour)
                if livre_a_retourner:
                    resultat_retour = livre_a_retourner.retourner()
                    print(resultat_retour)
                else:
                    print(f"Aucun livre trouvé avec le titre '{titre_retour}'")

            elif choix == "8":
                print("Fermeture de la bibliothèque.")
                break

            else:
                print("Choix invalide. Veuillez recommencer.")

if __name__ == "__main__":
    bibliotheque = Bibliotheque()
    bibliotheque.gerer_bibliotheque()
