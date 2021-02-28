from abc import abstractmethod

import core.models.grid as Grid


class Game:

    def __init__(self, board: Grid):
        self.board = board
        self.CubeArray = []

    def clear(self) -> bool:
        return self.board.fini()

    @abstractmethod
    def getscore(self):
        pass

    @abstractmethod
    def move(self, x, y):
        raise NotImplementedError

    def play(self):
        self.board.retrait_cubes(self.CubeArray)

