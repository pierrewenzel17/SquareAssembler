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
    def move(self, position):
        pass

    @abstractmethod
    def play(self):
        pass
