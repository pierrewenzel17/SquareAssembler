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
        self.score_controller.var_score.set("0")
        self.grid_controller.printgrid()

    def react_click(self, event):
        self.grid_effect(event)
        self.scor_effect()
        self.end_impact()




    def grid_effect(self,event):
        self.game.play()
        self.grid_controller.onHoveringEvent(event)

    def scor_effect(self):
        self.score_controller.var_score.set(self.game.getscore())

    def end_impact(self):
        if self.game.isclear():
            self.game.player.save_score()
            self.grid_controller.view.end_view()
