from client.controllers.grid_controller import GridController
from client.controllers.score_controller import ScoreController
from client.controllers.view_update import Observer


class GameController(Observer):

    def __init__(self, parent, game):
        self.game = game
        self.grid_controller = GridController(parent, self)
        self.grid_controller.printgrid()
        self.score_controller = ScoreController(parent)

    def update(self, data) -> None:
        self.game.board = data
        self.game.player.score = 0
        self.grid_controller.printgrid()
