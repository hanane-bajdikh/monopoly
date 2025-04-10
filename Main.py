from Joueur import Joueur
from Plateau import Plateau
from Partie import Partie
from random import randint


def initialiser_joueurs():

    """Fonction pour créer les joueurs."""
    noms_joueurs = ["Alice", "Bob", "Charlie"]
    return [Joueur(nom) for nom in noms_joueurs]


def selectionner_premier_joueur(liste_joueurs):

    """Sélectionner un joueur aléatoirement pour commencer."""
    return liste_joueurs[randint(0, len(liste_joueurs) - 1)]


def jouer_partie():
    
    """Fonction principale pour lancer la partie."""
    liste_joueurs = initialiser_joueurs()
    partie = Partie(liste_joueurs)

    joueur_actuel = selectionner_premier_joueur(liste_joueurs)
    print(f"Le premier joueur est {joueur_actuel.nom}.")

    jeu_termine = False
    while not jeu_termine:
        partie.tour(joueur_actuel)

        if partie.joueur_faillite():
            jeu_termine = True
            print(f"{joueur_actuel.nom} est en faillite !")
            break

        indice_prochain_joueur = (liste_joueurs.index(joueur_actuel) + 1) % len(liste_joueurs)
        joueur_actuel = liste_joueurs[indice_prochain_joueur]

    gagnant = partie.definir_gagnant()
    print(f"Le joueur gagnant est {gagnant.nom} avec {gagnant.argent}€.")

if __name__ == "__main__":
    jouer_partie()
