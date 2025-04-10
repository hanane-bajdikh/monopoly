from random import randint


class Joueur:


    def __init__(self, nom):
        # Initialisation du joueur avec son nom, son argent, sa position et ses propriétés
        self.nom = nom
        self.argent = 1500  # Montant d'argent initial
        self.position = 0  # Position initiale sur le plateau
        self.proprietes = []  # Liste des propriétés détenues par le joueur


    def tirer_de(self):
        # Tire un nombre aléatoire entre 1 et 6 pour simuler le dé
        return randint(1, 6)


    def deplacement(self, nb_cases, plateau):
        # Calcule la nouvelle position du joueur sur le plateau
        self.position = (self.position + nb_cases) % (len(plateau.liste_terrains) * len(plateau.liste_terrains[0]))

        # Calcul des coordonnées (i, j) sur le plateau
        i = self.position // len(plateau.liste_terrains[0])
        j = self.position % len(plateau.liste_terrains[0])

        print(f"{self.nom} avance de {nb_cases} cases et se trouve maintenant sur la case ({i}, {j}).")

        # Retourne le terrain sur lequel le joueur se trouve
        return plateau.avoir_terrain_i_j(i, j)


    def acheter(self, terrain):
        # Permet au joueur d'acheter un terrain s'il peut se le permettre
        if terrain.est_achetable() and self.argent >= terrain.prix_achat:
            self.argent -= terrain.prix_achat  # Déduit le prix d'achat de l'argent du joueur
            self.proprietes.append(terrain)  # Ajoute le terrain aux propriétés du joueur
            terrain.proprietaire = self  # Définit le joueur comme propriétaire du terrain
            print(f"{self.nom} a acheté le terrain {terrain.nom} pour {terrain.prix_achat}€.")
        else:
            print(f"{self.nom} ne peut pas acheter {terrain.nom}.")


    def payer(self, terrain, autre_joueur):
        # Permet au joueur de payer le loyer d'un terrain à un autre joueur
        if self.argent >= terrain.loyer:
            self.argent -= terrain.loyer  # Déduit le loyer de l'argent du joueur
            autre_joueur.argent += terrain.loyer  # Ajoute le loyer à l'argent de l'autre joueur
            print(f"{self.nom} paye {terrain.loyer}€ de loyer à {autre_joueur.nom} pour {terrain.nom}.")
        else:
            print(f"{self.nom} n'a pas assez d'argent pour payer le loyer.")
            self.faillite()  # Si pas assez d'argent, appelle la méthode de faillite


    def faillite(self):
        
        # Gère la situation de faillite du joueur
        print(f"{self.nom} est en faillite. Toutes ses propriétés sont remises en jeu.")
        
       
        for terrain in self.proprietes:
            terrain.proprietaire = None  # Réinitialise le propriétaire du terrain

        self.proprietes = []  # Vide la liste des propriétés du joueur


    def recevoir(self, montant):
        # Permet au joueur de recevoir un montant d'argent
        self.argent += montant
        print(f"{self.nom} reçoit {montant}€.")

