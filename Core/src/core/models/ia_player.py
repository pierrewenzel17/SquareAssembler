from core.models.player import Player
from core.models.human_player import HumanPlayer


class IaPlayer(Player):
    """Classe qui représente un joueur IA"""

    def __init__(self, player_id: int, name: str) -> None:
        """
        Constructeur
        :param player_id: un entier unique à chaque joueur
        :param name: le nom du joueur
        """
        super().__init__(player_id, name)

    def __eq__(self, ia_player: Player) -> bool:
        """
        Définition de l'opérateur ==, par consequent vérifie que l'IA courante
        est égal à l'IA passé en paramètre
        :param ia_player: L'IA  à tester
        :return: True ou False selon les valeurs des AI
        """
        if isinstance(ia_player, IaPlayer):
            return super().__eq__(ia_player)
        return False

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        return f"IA : {super().__str__()}"


# main de test pour la classe IaPlayer
if __name__ == '__main__':
    print("On test la classe IaPlayer")
    ia = IaPlayer(1, "test")
    ia2 = IaPlayer(1, "test")
    print("To string = " + str(ia))
    print("Equal : " + str(ia == ia2))
    ia2.id = 2
    print("Not Equal : " + str(ia != ia2))
    human = HumanPlayer(1, "test")
    print("Equal With Human : " + str(ia == human))
    human.id = 2
    print("Not Equal With Human : " + str(ia != human))

    print("On test la classe HumanPlayer")
    human = HumanPlayer(1, "test")
    human2 = HumanPlayer(1, "test")
    print("To string = " + str(human))
    print("Equal : " + str(human == human2))
    human.id = 2
    print("Not Equal : " + str(human != human2))
    ia = IaPlayer(1, "test")
    print("Equal With Human : " + str(ia == human))
    ia.id = 2
    print("Not Equal With Human : " + str(ia != human))
