import game as Game
import grid as Grid
import human_player as  Human_player
import player as Player


class GameOnePlayer(Game):

    def __init__(self, board: Grid, player: Player):
        super().__init__(board)
        self.__player = player

    def getscore(self):
        return self.__player.score

    def move(self, x, y):
        super.CubeArray = self.board.trouveforme(self.board[x, y], x, y)
        print(x)
    def play(self):
        super.play()
        self.__player.score = super.CubeArray.__len__()




