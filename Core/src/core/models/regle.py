from core.models import Grid ,Game

class Regle:


    def coup_valide(self) -> bool:
        """

        :param liste:  liste de ase dont il faut vérifier la validité
        :return:  true si la liste est composé d aux moins 3 élement , autrement return false
        """

        raise NotImplementedError


    def player_can_play(self):
        """
        fonction vérifiant si le joueur en cour peut jouer
        :param Game: parti en cour  , permet d'avoir l'accès au joueur et à la grille
        :return: true si les condition pour jouer son rempli
        """

        raise NotImplementedError


    def is_end_of_game(self):
        """
        vérifie si une partie et finie
        :param game:
        :return:
        """
        raise NotImplementedError


    def calcul_score(self):
        raise NotImplementedError
