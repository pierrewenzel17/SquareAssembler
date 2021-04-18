from abc import abstractmethod

import core.models.grid as Grid


class Game:

    def __init__(self, board: Grid):
        self.board :Grid= board
        self.CubeArray = []

    def isclear(self) -> bool:
        return self.board.fini()

    @abstractmethod
    def move(self, position):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def get_player_color(self):
        pass

    def coup_valide(self) -> bool:
        return len(self.CubeArray) > 2

    def get_time(self):
        return 0

    def reset_cube_array(self):
        self.CubeArray=[]

    @abstractmethod
    def game_master(self):
        pass