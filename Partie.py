import random
from Plateau import Plateau
from Terrain import Terrain


class Partie:
    
    
    def __init__(self, liste_joueur):
        # Initialisation de la partie avec une liste de joueurs et un plateau
        self.liste_joueur = liste_joueur
        self.plateau = Plateau()


    def avoir_joueur_avec_nom(self, nom):
        # Recherche un joueur par son nom et le retourne s'il existe
        return next((joueur for joueur in self.liste_joueur if joueur.nom == nom), None)


    def tour(self, joueur):
        # Gère le tour d'un joueur
        print(f"Tour de {joueur.nom}")

        # Tire le dé et détermine le déplacement
        deplacement = joueur.tirer_de()
        case_joueur = joueur.deplacement(deplacement, self.plateau)  # Déplace le joueur

        # Gérer les actions sur la case
        if isinstance(case_joueur, Terrain):
            self.traitement_post_deplacement(joueur, case_joueur)  # Traite le déplacement
            self.choisir_action(joueur, case_joueur)  # Propose une action au joueur


    def traitement_post_deplacement(self, joueur, terrain):
        # Traite les actions après le déplacement
        if terrain.est_achetable() and terrain.proprietaire is None:
            joueur.acheter(terrain)  # Le joueur achète le terrain s'il est disponible


    def choisir_action(self, joueur, terrain):
        # Propose des choix d'actions au joueur après son déplacement
        print(f"Options d'action pour {joueur.nom}:")
        print("1. Acheter le terrain")
        print("2. Passer")
        # Ajoutez d'autres options si nécessaire

        # Demande au joueur de faire un choix
        choix = input("Choisissez une action (1 ou 2) : ")

        if choix == "1":
            # Si le joueur choisit d'acheter le terrain
            if terrain.est_achetable() and terrain.proprietaire is None:
                joueur.acheter(terrain)
                print(f"{joueur.nom} a acheté {terrain.nom} !")
            else:
                print(f"{terrain.nom} n'est pas achetable ou a déjà un propriétaire.")

        elif choix == "2":
            # Si le joueur choisit de passer son tour
            print(f"{joueur.nom} passe son tour.")

        else:
            # Si le choix est invalide
            print("Choix invalide.")


    def joueur_faillite(self):
        # Vérifie si un joueur est en faillite
        return any(joueur.argent < 0 for joueur in self.liste_joueur)


    def definir_gagnant(self):
        # Détermine le joueur avec le plus d'argent comme gagnant
        return max(self.liste_joueur, key=lambda joueur: joueur.argent)
