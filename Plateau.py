from Terrain import Terrain
from Case_speciale import Case_speciale


class Plateau:


    def __init__(self):
        
        # Initialise le plateau avec une liste de terrains
        self.liste_terrains = [
            [
                # Case spéciale "Départ" qui donne 200€ au joueur
                Case_speciale("Départ", lambda joueur: joueur.recevoir(200)),

                # Terrains classiques avec leur nom, couleur, prix d'achat et loyer
                Terrain("Boulevard de Belleville", "marron", 50, 4),
                Terrain("Rue Lecourbe", "marron", 50, 4),
                Case_speciale("GM", lambda joueur: None),  # Case spéciale GM avec action par défaut

                Terrain("Rue de Vaugirard", "bleu", 100, 6),
                Terrain("Rue de Courcelles", "bleu", 100, 6),
                Terrain("Avenue de la République", "bleu", 100, 6)
            ]
        ]

    def avoir_terrain_i_j(self, i, j):
       
        # Renvoie le terrain se trouvant aux coordonnées (i, j) sur le plateau
        if 0 <= i < len(self.liste_terrains) and 0 <= j < len(self.liste_terrains[i]):
            return self.liste_terrains[i][j]
        else:
            raise IndexError("Coordonnées en dehors des limites du plateau.")  # Gère les coordonnées invalides
