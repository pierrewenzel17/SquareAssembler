from tkinter import Tk

from client.controllers.game_controller import GameController
from client.controllers.menu_controller import MenuController
from client.utils.constant_util import Constants
from client.views.main_frame_view import MainFrameView
from core.models.gameOnePlayer import GameOnePlayer
from core.models.grid import Grid
from core.models.human_player import HumanPlayer


class MainController:

    def __init__(self, mainFrame, grid ):
        self.mainFrame = mainFrame
        player = HumanPlayer(69, "test")
        self.view = MainFrameView(self.mainFrame, self)
        self.menu_controller = MenuController(self.mainFrame, player)
        self.game_controller = GameController(self.mainFrame, GameOnePlayer(grid,
                                                                            player))
        self.menu_controller.add_observer(self.game_controller)

    def run(self):
        self.mainFrame.mainloop()
