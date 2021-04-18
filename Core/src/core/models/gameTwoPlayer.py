from core.models.color import Color
from core.models.game import Game
from core.models.grid import Grid
from core.models.player import Player
from core.models.cube import Cube
from core.models.human_player import HumanPlayer
from core.models.position import Position


class GameTwoPlayer(Game):
    def __init__(self, board: Grid, player1: Player, time: int):
        ## player = 0 player2 = 1
        super().__init__(board)
        self.turn = 0
        self.__player = []
        self.__player.append(player1)
        player2 = Player(1, "adversair")
        self.__player.append(player2)
        self.__colorallouer = [[], []]

        self.__time = time

    def getscore(self):
        return self.__player[0].score

    def getPlayer(self):
        return self.__player[self.turn]

    def getTurn(self):
        return self.turn

    def getColorMax(self):
        return self.board.getNbcolor() / 2

    def chekColorattribut(self, couleur):
        if len(self.__colorallouer[self.getTurn()]) < self.getColorMax():
            if couleur not in self.__colorallouer[self.getTurn()] \
                    and couleur not in self.__colorallouer[self.otherPlayer()]:
                self.__colorallouer[self.getTurn()].append(couleur)

    def validColor(self, cube: Cube):
        if cube is None:
            return False
        else:
            return self.__verif_color(cube.color)

    def otherPlayer(self):
        if self.getTurn() == 0:
            return 1
        else:
            return 0

    def changeTurn(self, isturn: bool):
        '''

        :param isturn: booléein récupéré depuis le controleur indique si c'est notre tour ou celui de l'adversaire
        :return:
        '''
        if isturn:
            self.turn = 0
        else:
            self.turn = 1

    def move(self, position):
        cube = self.board[position.i, position.j]
        liste = self.board.trouve_forme(self.board[position.i, position.j], position.i, position.j)
        self.board.demarcage(liste)
        # verifier aussi que la couleur est soit libre soit prise par le joueur qui joue le tour
        if len(liste) > 2 and self.validColor(cube):
            self.CubeArray = liste
        else:
            self.CubeArray = []

    def play(self):
        vecteur = self.CubeArray[0]
        couleur = self.board[vecteur.i, vecteur.j].color
        self.board.retrait_cubes(self.CubeArray)
        self.__player[self.getTurn()].score += len(self.CubeArray)
        ## verifier si le joueur qui cjoue posssège la coueur ,si non lui ajouter
        self.chekColorattribut(couleur)


    def playercanplay(self):
        return self.board.parcourt(lambda x: self.couposible(x))

    def couposible(self, liste):
        if len(liste) > 2:
            vecteur = liste[0]
            cube = self.board[vecteur.i, vecteur.j]
            return self.validColor(cube)
        return False

    def get_player_color(self):
        liste_color: list = Color.Getall()
        list_final: list = []
        for i in range(0, self.board.getNbcolor()):
            if self.__verif_color(liste_color[i]):
                list_final.append(liste_color[i])
        return list_final

    def get_time(self):
        return self.__time
    def __verif_color(self, color):
        if len(self.__colorallouer[self.getTurn()]) == self.getColorMax():
            return True if color in self.__colorallouer[self.getTurn()] else False
        else:
            return False if color in self.__colorallouer[self.otherPlayer()] else True

    def game_master(self):
        return self.__player[0]

if __name__ == '__main__':
    print("On test la classe game2jpueur")
    player1 = HumanPlayer(69, "test")
    player2 = HumanPlayer(6, "drogue")
    board = Grid.grid_by_ten()
    game = GameTwoPlayer(board, player1, player2, 10)
    while not game.isclear():
        print(game.board)
        print("au tour du joueur : ")
        x = input("On veut quel ligne ?")
        y = input("On veut quel colonne ?")
        game.move(Position(int(x), int(y)))
        game.play()
