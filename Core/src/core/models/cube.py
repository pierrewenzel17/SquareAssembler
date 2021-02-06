from core.models import Color
from core.models import Position


class Cube:
    """Classe qui représente un Cube"""

    def __init__(self, color: Color) -> None:
        """
        Constructeur
        :param color: La couleur du cube
        """
        self.color = color
        self.visite=True

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        return f" color = {self.color}"

    def __eq__(self, cube: 'Cube') -> bool:
        """
        Définition de l'opérateur ==, par consequent vérifie que le cube courant
        est égal au cube passé en paramètre
        :param cube: Le cube à tester
        :return: True ou False selon les valeurs des cubes
        """
        return self.color == cube.color

    def __ne__(self, cube: 'Cube') -> bool:
        """
        Définition de l'opérateur !=, par consequent vérifie que le cube courant
        est différent du cube passé en paramètre
        :param cube: Le cube à tester
        :return: True ou False selon les valeurs des cubes
        """
        return not self == cube

    def have_same_color(self, cube: 'Cube') -> bool:
        """
        Fonction qui vérifie que la couleur du cube courant est égal à la couleur du cube passé en paramètre
        :param cube: le cube dont la couleur doit être comparé
        :return: True ou False selon les valeurs des couleurs
        """
        return self.color == cube.color


    def est_visitable(self) -> bool:
        """

        :return: True si le cube n'a pas été visité , False si il a déjà  été visité
        """
        return self.visite


    def setvisitable(self, bol: bool):
        """

        :param bol:  valeur  booleein  qui va remplacer l'ancienne
        :return:  rien
        """
        self.visite = bol

# main de test pour la classe Cube
if __name__ == '__main__':
    print("On test la classe cube")
    c1 = Cube( color=Color.RED)
    c2 = Cube( color=Color.RED)
    # On  test ici le to_string
    print(c1)
    # On test ici la fonction equal
    print(c1 == c2)
    # On test ici la fonction have_same_color
    print(c1.have_same_color(c2))
    c2.color = Color.BLUE
    # On test ici la fonction not equal
    print(c1 != c2)
