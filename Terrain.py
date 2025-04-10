class Terrain:
    def __init__(self, nom, couleur, prix_achat, loyer):
        self.nom = nom
        self.couleur = couleur
        self.prix_achat = prix_achat
        self.loyer = loyer
        self.proprietaire = None

    def est_achetable(self):
        return self.proprietaire is None
