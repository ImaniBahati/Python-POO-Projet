#coding by Faith

import random

class Compte:
    def __init__(self, numero_compte, nom_proprietaire_compte, solde_compte, pin):
        self.numero_compte = numero_compte
        self.nom_proprietaire_compte = nom_proprietaire_compte
        self.solde_compte = solde_compte
        self.pin = pin

    def depot(self, montant):
        self.solde_compte += montant

    def retrait(self, montant, pin):
        if pin == self.pin:
            if montant <= self.solde_compte:
                self.solde_compte -= montant
                print(f"Retrait de {montant} effectué avec succès.")
            else:
                print("Solde insuffisant.")
        else:
            print("Code PIN incorrect. Opération annulée.")

    def get_balance(self):
        return self.solde_compte

    def __str__(self):
        return f"Compte numéro {self.numero_compte}: Propriétaire - {self.nom_proprietaire_compte}, Solde - {self.solde_compte}"


class Banque:
    def __init__(self):
        self.comptes = {}

    def cree_compte(self, numero_compte, nom_proprietaire_compte, balance_initiale, pin):
        if numero_compte in self.comptes:
            print("Le numéro de compte existe déjà.")
        else:
            compte = Compte(numero_compte, nom_proprietaire_compte, balance_initiale, pin)
            self.comptes[numero_compte] = compte
            print(f"Compte créé avec succès. Code PIN : {pin}")

    def get_compte(self, numero_compte):
        compte = self.comptes.get(numero_compte)
        if compte:
            return compte
        else:
            print("Le numéro de compte est invalide.")
            return None

    def depot(self, numero_compte, montant):
        compte = self.get_compte(numero_compte)
        if compte:
            compte.depot(montant)
            print(f"Dépôt de {montant} effectué avec succès. Solde actuel : {compte.get_balance()}")

    def retrait(self, numero_compte, montant, pin):
        compte = self.get_compte(numero_compte)
        if compte:
            compte.retrait(montant, pin)
            print(f"Solde actuel : {compte.get_balance()}")

    def get_balance(self, numero_compte):
        compte = self.get_compte(numero_compte)
        if compte:
            print(f"Solde actuel : {compte.get_balance()}")

    def transfert(self, du_numero_compte, au_numero_compte, montant, pin):
        compte_source = self.get_compte(du_numero_compte)
        compte_destination = self.get_compte(au_numero_compte)
        
        if compte_source and compte_destination:
            if compte_source.pin == pin:
                if montant <= compte_source.get_balance():
                    compte_source.retrait(montant, pin)
                    compte_destination.depot(montant)
                    print(f"Transfert de {montant} effectué avec succès vers le compte {au_numero_compte}.")
                else:
                    print("Solde insuffisant pour effectuer le transfert.")
            else:
                print("Code PIN incorrect. Opération annulée.")
        else:
            print("Numéro de compte invalide.")

    def supprimer_compte(self, numero_compte, pin):
        compte = self.get_compte(numero_compte)
        if compte:
            if compte.pin == pin:
                del self.comptes[numero_compte]
                print("Compte supprimé avec succès.")
            else:
                print("Code PIN incorrect. Opération annulée.")

class GestionnaireCompte:
    def __init__(self, banque):
        self.banque = banque

    def authentification(self, numero_compte, pin):
        compte = self.banque.get_compte(numero_compte)
        if compte and compte.pin == pin:
            print("Authentification réussie.")
            return True
        else:
            print("Authentification échouée.")
            return False

    def generate_random_pin(self):
        return str(random.randint(1000, 9999))

banque = Banque()
gestionnaire = GestionnaireCompte(banque)

while True:
    print("Bienvenue dans notre système bancaire ! Que souhaitez-vous faire ?")
    print("1. Créer un compte")
    print("2. Se connecter à un compte")
    print("3. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        numero_compte = input("Entrez le numéro de compte : ")
        nom_proprietaire_compte = input("Entrez le nom du titulaire du compte : ")
        balance_initiale = float(input("Entrez le solde initial : "))
        pin = gestionnaire.generate_random_pin()
        banque.cree_compte(numero_compte, nom_proprietaire_compte, balance_initiale, pin)
    elif choix == "2":
        numero_compte = input("Entrez le numéro de compte : ")
        pin = input("Entrez votre code PIN : ")
        if gestionnaire.authentification(numero_compte, pin):
            while True:
                print("Bienvenue dans votre compte bancaire ! Que souhaitez-vous faire ?")
                print("1. Faire un dépôt")
                print("2. Faire un retrait")
                print("3. Effectuer un transfert")
                print("4. Consulter le solde")
                print("5. Supprimer le compte")
                print("6. Se déconnecter")

                choix_operation = input("Votre choix : ")

                if choix_operation == "1":
                    montant = float(input("Entrez le montant à déposer : "))
                    banque.depot(numero_compte, montant)
                elif choix_operation == "2":
                    montant = float(input("Entrez le montant à retirer : "))
                    pin = input("Entrez votre code PIN : ")
                    banque.retrait(numero_compte, montant, pin)
                elif choix_operation == "3":
                    montant = float(input("Entrez le montant à transférer : "))
                    pin = input("Entrez votre code PIN : ")
                    compte_destination = input("Entrez le numéro de compte du destinataire : ")
                    banque.transfert(numero_compte, compte_destination, montant, pin)
                elif choix_operation == "4":
                    banque.get_balance(numero_compte)
                elif choix_operation == "5":
                    pin = input("Entrez votre code PIN : ")
                    banque.supprimer_compte(numero_compte, pin)
                    break
                elif choix_operation == "6":
                    break
                else:
                    print("Opération invalide. Veuillez choisir une option valide.")
    elif choix == "3":
        print("Merci d'utiliser notre système bancaire. Au revoir !")
        break
    else:
        print("Opération invalide. Veuillez choisir une option valide.")

