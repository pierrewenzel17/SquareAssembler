import core.models.grid as Grid


class Player:
    """
    Classe mère qui représente un joueur
    N'a pas vocation à être instancié
    """

    def __init__(self, player_id: int, name: str) -> None:
        """
        Constructeur
        :param player_id: L'identifiant unique du joueur
        :param name: Le nom du joueur
        """
        self.id = player_id
        self.name = name
        self.score = 0

    def __eq__(self, player: 'Player') -> bool:
        """
        Définition de l'opérateur ==, par consequent vérifie que le joueur courant
        est égal au joueur passé en paramètre
        :param player: Le joueur à tester
        :return: True ou False selon les valeurs des joueurs
        """
        return self.id == player.id

    def __ne__(self, player: 'Player') -> bool:
        """
        Définition de l'opérateur !=, par consequent vérifie que le joueur courant
        est différent au joueur passé en paramètre
        :param player: Le joueur à tester
        :return: True ou False selon les valeurs des joueurs
        """
        return not self == player

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        return f"id = {self.id}, nom = {self.name}, score = {self.score}"

    def increment_score(self, value: int) -> None:
        """
        Fonction qui incrémente le score
        :param value: la valeur dont il faut incrémenté
        """
        self.score += value

    def play(self, board: Grid) -> []:
        """
        fonction abstrait qui permet à un joueur de jouer
        :param board:
        :return:
        """
        raise NotImplementedError
