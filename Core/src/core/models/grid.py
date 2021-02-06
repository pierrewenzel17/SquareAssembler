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

    def trouve_forme(self, cube, x, y) -> []:
        """

        :param colorcube:
        :param x:
        :param y:
        :return:
        """
        if x < 0 or y < 0 or x >= self.nb_col_row or y >= self.nb_col_row:
            return []
        elif self[x, y] is None or cube is None:
            return []
        elif self[x, y].color == cube.color and self[x, y].est_visitable():
            self[x, y].setvisitable(False)
            tab_cube = []
            tab_cube.append(Position(x, y))
            left = self.trouve_forme(cube, x - 1, y)
            rigth = self.trouve_forme(cube, x + 1, y)
            down = self.trouve_forme(cube, x, y + 1)
            up = self.trouve_forme(cube, x, y - 1)
            tab_cube.extend(up)
            tab_cube.extend(down)
            tab_cube.extend(left)
            tab_cube.extend(rigth)
            return tab_cube
        else:
            return []

    def __clear_cube_fantome(self, position):
        """

        :param cube: cube qui a était supprimer :sert de réference pour conettre la colone ou il y a un ccube en trops
        :return:
        """
        i = 0
        while self.matrix[i][position.y] is None:
            i = i + 1
        self.matrix[i][position.y] = None

    def retrait_cubes(self, tab_cube):
        for position in tab_cube:
            x = position.x
            'pour chaque cube à suprimer  on fait décendre les cubes qui sont au dessus '
            while x > 0 and self[x - 1, position.y] is not None:
                self[x, position.y] = self[x - 1, position.y]
                x = x - 1
            ' one foie le decalge effectuer on retire le cube (residuele le plus haut) '
        for cube in tab_cube:
            self.clear_cube_fantome(cube)
        for cube in tab_cube:
            self.retrait_colonne_vide(cube.y)

    def __colone_est_vide(self, y) -> bool:
        check = True
        x = 0
        while check and x < self.nb_col_row:
            if self[x, y] is not None:
                check = False
            x += 1
        return check

    def __destruct_last_colunn(self):
        for x in range(0, self.nb_col_row):
            self[x, self.nb_col_row - 1] = None

    def __retrait_colonne_vide(self, y):
        if self.__colone_est_vide(y):
            for col in range(y, self.nb_col_row - 1):
                for ligne in range(0, self.nb_col_row):
                    self[ligne, col] = self[ligne, col + 1]
            self.__destruct_last_colunn()

    def demarcage(self, liste):
        for position in liste:
            x, y = position.x, position.y
            self[x, y].setvisitable(True)

    def fini(self) -> bool:
        '''

        :return: un booléain indiquant la fin de la partie
        '''
        for x in range(0, self.nb_col_row):
            for y in range(0, self.nb_col_row):
                liste = self.trouve_forme(self[x, y], x, y)
                self.demarcage(liste)
                if (len(liste) >= 2):
                    return False
        return True

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
