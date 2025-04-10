class Case_speciale:
    
    def __init__(self, nom, action):
        # Initialise une case spéciale avec un nom et une action à effectuer
        self.nom = nom
        self.action = action

    def activer(self, joueur):
        # Active l'action de la case spéciale pour un joueur donné
        self.action(joueur)

# Fonction qui envoie le joueur directement en prison
def envoyer_en_prison(joueur):
    joueur.position = "Prison"  # Change la position du joueur en "Prison"
    print(f"{joueur.nom} va directement en prison ! Ne passez pas par la case Départ, ne touchez pas 200€.")

# Fonction qui permet au joueur de recevoir 200€
def recevoir_200_euros(joueur):
    joueur.recevoir(200)  # Utilise la méthode recevoir du joueur pour ajouter 200€

# Définition des cases spéciales
case_prison = Case_speciale("Prison", envoyer_en_prison)  # Case qui envoie en prison
case_depart = Case_speciale("Départ", recevoir_200_euros)  # Case qui donne 200€ au joueur
