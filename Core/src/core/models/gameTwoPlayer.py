import core.models.game as Game
import core.models.grid as Grid
import core.models.player as Player


class GameTwoPlayer(Game):
    def __init__(self, board: Grid, player1: Player, player2: Player, time : int ):

        super().__init__(board)
        self.__player1 = player1
        self.__player2 = player2
        self.__player1color = []
        self.__player2color = []
        self.__time = time

def getscore(self):
    return self.__player.score
