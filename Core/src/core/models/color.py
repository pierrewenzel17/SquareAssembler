from enum import Enum
import random


class Color(Enum):
    """Énumération des couleurs que peuvent prendre un Cube"""
    RED = "#FF0000"
    BLUE = "#07ACF4"
    GREEN = "#25D147"
    ORANGE = "#FE6C00"
    PURPLE = "#A30571"
    BROWN = "#C17A06"
    YELLOW = "#F3FF00"
    PINK = "#EB58E9"

    def __eq__(self, color: Enum) -> bool:
        """
        Définition de l'opérateur ==, par consequent vérifie que la couleur courant
        est égal à la couleur passé en paramètre
        :param color: La couleur à tester
        :return: True ou False selon les valeurs des couleurs
        """
        return self.name == color.name

    def __ne__(self, color: Enum) -> bool:
        """
        Définition de l'opérateur !=, par consequent vérifie que la couleur courant
        est différente à la couleur passé en paramètre
        :param color: La couleur à tester
        :return: True ou False selon les valeurs des couleurs
        """
        return not self.name == color.name

    @staticmethod
    def __get_list_of_first(nb: int) -> list:
        """
        Fonction qui crée une liste de couleur
        :param nb: Le nombre de couleur à avoir dans la liste
        :return: La liste des couleurs
        """
        color_list, i = [], 0
        for color in Color:
            if i == nb:
                break
            color_list.append(color)
            i += 1
        return color_list

    @staticmethod
    def get_dict_color(nb: int, grid_len: int) -> dict:
        """
        Fonction qui donne le nombre d'occurrence nécessaire des couleurs dans une grille en fonction de la taille de
        la grille
        :param nb: le nombre de couleurs voulu
        :param grid_len: la taille de la grille
        :return: un dictionnaire dont la clef est la couleur et la valeur, le nombre d'occurrences nécessaire
        """

        color_list: list = Color.__get_list_of_first(nb)
        nb_type_color: int = grid_len * grid_len // nb
        return_color: dict = {}

        for color in color_list:
            return_color[color] = nb_type_color
        return return_color

    @staticmethod
    def Getall():
        return  Color.__get_list_of_first(8)
    @staticmethod
    def get_random_color(dict_color: dict) -> 'Color':
        """
        Fonction prend au hasard une couleur si elle est disponible
        :param dict_color: un dictionnaire dont la clef est une couleur et la valeur ne nombre
         d'occurrence possible de cette couleur
        :return: la couleur choisi aléatoirement
        """
        color: 'Color' = random.choice(list(dict_color.keys()))
        dict_color[color] -= 1

        if dict_color[color] == 0:
            del dict_color[color]
        return color

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        return f"{self.name}"

    def __hash__(self):
        """
        Fonction de hachage
        :return: le hache d'une couleur
        """
        return hash(self.name)


# main de test pour l'énumération des couleurs
if __name__ == '__main__':
    print("On test ici l'énumération couleur")
    c1 = Color.RED
    c2 = Color.RED
    # On test ici le to_string et la valeur de l'élément
    print("le nom " + str(c1) + " la valeur : " + str(c1.value))
    # On test ici la fonction equal
    print(c1 == c2)
    c2 = Color.BROWN
    # On test ici la fonction not equal
    print(c1 != c2)
