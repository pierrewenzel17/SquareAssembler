import grid as Grid


class Game:

    def __init__(self, board: Grid):
        self.board = board
        self.CubeArray = []

    def clear(self) -> bool:
        return self.board.fini()

    def getscore(self):
        raise NotImplementedError

    def move(self, x, y):
        raise NotImplementedError
    def play(self ):
        self.board.retrait_cubes(self.CubeArray)

