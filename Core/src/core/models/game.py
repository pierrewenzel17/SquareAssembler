from abc import abstractmethod

import core.models.grid as Grid


class Game:

    def __init__(self, board: Grid):
        self.board = board
        self.CubeArray = []

    def isclear(self) -> bool:
        return self.board.fini()


    @abstractmethod
    def move(self, position):
        pass

    @abstractmethod
    def play(self):
        pass
