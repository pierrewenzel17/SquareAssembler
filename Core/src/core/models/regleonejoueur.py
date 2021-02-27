from abc import ABC

from core.models import Regle


class RegleunJoueur(Regle):

    def calcul_score(self):
        pass

    def is_end_of_game(self):
        pass

    def coup_valide(self) -> bool:
        pass

    def player_can_play(self):
        """
        fonction vérifiant si le joueur en cour peut jouer
        :param Game: parti en cour  , permet d'avoir l'accès au joueur et à la grille
        :return: true si les condition pour jouer son rempli
        """

        raise NotImplementedError


