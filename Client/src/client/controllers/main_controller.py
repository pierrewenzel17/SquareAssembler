from client.controllers.game_controller import GameController
from client.controllers.grid_controller import GridController
from client.controllers.menu_controller import MenuController
from client.controllers.score_controller import ScoreController
from client.views.main_frame_view import MainFrameView
from core.models.gameOnePlayer import GameOnePlayer
from core.models.grid import Grid
from core.models.human_player import HumanPlayer


class MainController:

    def __init__(self, root):
        self.parent = root
        self.view = MainFrameView(self.parent, self)
        self.menu_controller = MenuController(self.parent)
        self.game_controller = GameController(self.parent, GameOnePlayer(Grid.grid_by_ten(),
                                                                         HumanPlayer(69, "test")))
        self.menu_controller.add_observer(self.game_controller)
    def run(self):
        self.parent.mainloop()
