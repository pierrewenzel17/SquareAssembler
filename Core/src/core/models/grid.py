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
                row.append(Cube(color=Color.get_random_color(dict_color)))
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
                if value is None:
                    string_builder += "|None"
                else:
                    string_builder += "|" + cs("cube", value.color.value)
            string_builder += "|\n"
        return string_builder

    def trouve_forme(self, cube, x, y) -> []:
        """
        fonction recherchant une  suite de cube de même couleur à partir d'une case de la grille
        :param cube:  cube de référence ,permet de connaitre la couleur souhaité
        :param x: la cordoné sur l'axe des i
        :param y: ma coordonnée sur l'axe des j
        :return: une liste de position
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
        fonction qui efface les cube qui n'ont plus lieux d'être
        :param cube: cube qui a était supprimer :sert de réference pour conettre la colone ou il y a un cube en trops
        :return:
        """
        i = 0
        while self[i, position.j] is None:
            i = i + 1
        self[i, position.j] = None

    def retrait_cubes(self, tab_position):
        """
        fonction effectuant la suppression des cubes
        :param tab_position:  tableau de Positiion , contenant le position des cube à
        supprimer
        :return:
        """
        tab_position.sort()
        for position in tab_position:
            x = position.i
            'pour chaque cube à suprimer  on fait décendre les cubes qui sont au dessus '
            while x > 0 and self[x - 1, position.j] is not None:
                self[x, position.j] = self[x - 1, position.j]
                x = x - 1
            ' one foie le decalge effectuer on retire le cube (residuele le plus haut) '
        for position in tab_position:
            self.__clear_cube_fantome(position)
            ' enfin on vérifie si la supresion des cube à engendré une colonne vide  et on la suprimme si c est le cas'
        for position in tab_position:
            self.__retrait_colonne_vide(position.j)

    def __colone_est_vide(self, y: int) -> bool:
        """
        fonction vérifiant si une colone est vide
        :param y:  numéro de la colonne que l'on souhaite vérifier
        :return:  True si la colonne est vide , sinon false
        """
        check = True
        x = 0
        while check and x < self.nb_col_row:
            if self[x, y] is not None:
                check = False
            x += 1
        return check

    def __destruct_last_colunn(self):
        """
        fonction qui d'étruit la dernière colonne de la grille , nesert qu'une foispar partie ,
        au moment de la supression de la première colone vide

        """
        for x in range(0, self.nb_col_row):
            self[x, self.nb_col_row - 1] = None

    def __retrait_colonne_vide(self, y):
        """
        fonction qui enlève la  colonne y ,si elle est vide,  et décale les colones à droite de la colonne
        y sur la gauche
        :param y:   numéro de la colone vérifier
        :return:
        """
        if self.__colone_est_vide(y):
            for col in range(y, self.nb_col_row - 1):
                for ligne in range(0, self.nb_col_row):
                    self[ligne, col] = self[ligne, col + 1]
            self.__destruct_last_colunn()

    def demarcage(self, liste):
        """
        fonction qui reset le booléen utile à la fonction de parcourt de graphe :'trouveforme '
        :param liste:
        :return:
        """
        for position in liste:
            x, y = position.i, position.j
            self[x, y].setvisitable(True)

    def fini(self) -> bool:
        '''
        fonction vérifiant la fin de la partie
        :return: true si il  reste plus de coup à jouer ,  sinon false
        '''
        for x in range(0, self.nb_col_row):
            for y in range(0, self.nb_col_row):
                liste = self.trouve_forme(self[x, y], x, y)
                self.demarcage(liste)
                if self.coup_valide(liste):
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

    def coup_valide(self, liste) -> bool:
        """

        :param liste:  liste de ase dont il faut vérifier la validité
        :return:  true si la liste est composé d aux moins 3 élement , autrement return false
        """
        return len(liste) >= 3


# main de test pour la classe Grille
if __name__ == '__main__':
    print("On test la classe grille")
    grid_10 = Grid.grid_by_ten()
    print(grid_10)
    grid_20 = Grid.grid_by_twenty()
    print(grid_20)
    print("test " + str(grid_10[0, 0]))

    for cube in grid_10:
        print(cube)

    # simulation d'ue partie
    while not grid_10.fini():
        print(grid_10)
        l = 0
        liste = []
        while l < 2:
            x = input("On veut quel ligne ?")
            y = input("On veut quel colonne ?")
            liste = grid_10.trouve_forme(grid_10[int(x), int(y)], int(x), int(y))
            l = len(liste)
            grid_10.demarcage(liste)
        grid_10.retrait_cubes(liste)
    print("end game")
