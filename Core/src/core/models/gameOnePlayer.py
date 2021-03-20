from core.models.game import Game
from core.models.grid import Grid
from core.models.player import Player



class GameOnePlayer(Game):

    def __init__(self, board: Grid, player: Player):
        super().__init__(board)
        self.player = player

    def getscore(self):
        return self.player.score

    def move(self, position):
        liste = self.board.trouve_forme(self.board[position.i, position.j], position.i, position.j)
        self.board.demarcage(liste)
        if len(liste) > 2:
            self.CubeArray=liste
        else:
            self.CubeArray = []

    def play(self):
        self.board.retrait_cubes(self.CubeArray)
        print()
        self.player.score += len(self.CubeArray)
