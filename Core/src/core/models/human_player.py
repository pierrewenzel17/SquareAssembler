from core.models.player import Player


class HumanPlayer(Player):
    """Classe qui représente un joueur humain"""

    def __init__(self, player_id: int, name: str) -> None:
        """
        Constructeur
        :param player_id: un entier unique à chaque joueur
        :param name: le nom du joueur
        """
        super().__init__(player_id, name)
        self.tab_score=[]

    def __eq__(self, human_player: Player) -> bool:
        """
        Définition de l'opérateur ==, par consequent vérifie que la personne courante
        est égal à la personne passé en paramètre
        :param human_player: La personne à tester
        :return: True ou False selon les valeurs des personnes
        """
        if isinstance(human_player, HumanPlayer):
            return super().__eq__(human_player)
        return False

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        sting= f"Humain : {super().__str__()}"
        for score in self.tab_score:
            sting += f" {score} "
        return sting

    def save_score(self):
        self.tab_score.append(self.score)