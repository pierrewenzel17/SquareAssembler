from stringcolor import cs
from core.models import Cube, Position, Color


class Grid:
    """Classe qui représente une grille"""

    def __init__(self, nb_col_row: int, number_of_color: int) -> None:
        """
        Constructeur
        :param nb_col_row: nombre le ligne - colonne, la grille est toujours un carré ex : 10*10 ou 20*20
        :param number_of_color: nombre de couleurs différentes dans la grille
        """
        self.nb_col_row, self.__matrix = nb_col_row, []
        self.__i = self.__j = 0
        dict_color: dict = Color.get_dict_color(number_of_color, nb_col_row)
        for i in range(0, nb_col_row):
            row = []
            for j in range(0, nb_col_row):
                row.append(Cube(position=Position(i, j), color=Color.get_random_color(dict_color)))
            self.__matrix.append(row)

    def __getitem__(self, tup: tuple) -> Cube:
        """
        Opérateur [] qui permet d'accédé à un élément de la grille
        :param tup: contient les coordonnées du cube dans la grille exemple : [1, 2]
        :return: le cube
        :rtype: Cube
        """
        i, j = tup
        return self.__matrix[i][j]

    def __setitem__(self, tup: tuple, value: Cube) -> None:
        """
        Opérateur [] = qui permet d'initialiser ou de modifier un élément de la grille
        exemple : grid[1, 1] = my_cube
        :param tup: contient les coordonnées du cube dans la grille exemple : [1, 2]
        :param value: le cube à affecter à la grille
        """
        i, j = tup
        self.__matrix[i][j] = value

    def __iter__(self):
        """
        Définition de l'opérateur d'itération sur la classe Grille
        """
        return self

    def __next__(self) -> Cube:
        """
        Définition du suivant
        exemple : for cube in grid:
                    print(cube)
        :return: le cube qui est demander par l'itérateur
        :raise stop l'itérateur quand il n'y a plus d'élément sur lequel itéré
        """
        while self.__i < self.nb_col_row:
            if self.__j < self.nb_col_row:
                j = self.__j
                self.__j += 1
                return self.__matrix[self.__i][j]
            else:
                self.__i += 1
                self.__j = 0
        self.__i = self.__j = 0
        raise StopIteration()

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        string_builder = ""
        for row in self.__matrix:
            for value in row:
                string_builder += "|" + cs("cube", value.color.value)
            string_builder += "|\n"
        return string_builder

    @classmethod
    def grid_by_ten(cls) -> 'Grid':
        """
        Constructeur par défaut d'une grille 10*10 avec 4 couleurs
        :return: la grille initialisée
        """
        return cls(10, 4)

    @classmethod
    def grid_by_twenty(cls) -> 'Grid':
        """
        Constructeur par défaut d'une grille 20*20 avec 8 couleurs
        :return: la grille initialisée
        """
        return cls(20, 8)


# main de test pour la classe Grille
if __name__ == '__main__':
    print("On test la classe grille")
    grid_10: Grid = Grid.grid_by_ten()
    print(grid_10)
    grid_20 = Grid.grid_by_twenty()
    print(grid_20)
    print("test " + str(grid_10[0, 0]))

    for cube in grid_10:
        print(cube)
