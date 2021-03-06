class Position:
    """Classe qui représente une position dans une Matrice / Grille"""

    def __init__(self, i: int, j: int) -> None:
        """
        Constructeur
        :rtype: object
        :param x: coordonnée en X
        :param y: coordonnée en Y   ( ceci n 'a  aucun sens )
        """
        self.i, self.j = i, j

    def __eq__(self, position: 'Position') -> bool:
        """
        Définition de l'opérateur ==, par consequent vérifie que la position courant
        est égal à la position passé en paramètre
        :param position: La position à tester
        :return: True ou False selon les valeurs de position
        """
        return self.i == position.i and self.j == position.j

    def __ne__(self, position: 'Position') -> bool:
        """
        Définition de l'opérateur !=, par consequent vérifie que la position courant
        est différente à la position passé en paramètre
        :param position: La position à tester
        :return: True ou False selon les valeurs de position
        """
        return not self == position

    def __str__(self) -> str:
        """
        Méthode to string
        :return: la classe sous forme de string
        """
        return f"i = {self.i}, j = {self.j}"

    def __lt__(self, o: object) -> bool:
        """
         Définition de l'opérateur <, par consequent vérifie que la position courant
        est inférieur  à la position passé en paramètre , la vérification ce fait par rapport a l'axe des i !!!!!
        :param position: La position à tester
        :return: True ou False selon les valeurs de position . si self.i<position.i alors True sinon false
        """
        if self.i == o.i:
            return self.j > o.j
        else:
            return self.i < o.i


# main de test pour la classe Position
if __name__ == '__main__':
    print("On test de la classe Position")
    p1 = Position(1, 3)
    p2 = Position(1, 3)
    # On test le to_string
    print(p1)
    # On test le equal
    print(p2 == p1)
    p2.i = 2
    # On test le not equal
    print(p2 != p1)
