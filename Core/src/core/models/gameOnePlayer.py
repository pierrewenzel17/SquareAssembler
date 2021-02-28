from core.models.game import Game
from core.models.grid import Grid
from core.models.player import Player
from core.models.human_player import HumanPlayer


class GameOnePlayer(Game):

    def __init__(self, board: Grid, player: Player):
        super().__init__(board)
        self.__player = player

    def getscore(self):
        return self.__player.score

    def move(self, x, y):
        super().CubeArray = self.board.trouveforme(self.board[x, y], x, y)
        print(x)

    def play(self):
        self.__player.score = super().CubeArray.__len__()

