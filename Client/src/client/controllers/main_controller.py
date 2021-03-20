from tkinter import Tk

from client.controllers.game_controller import GameController
from client.controllers.menu_controller import MenuController
from client.views.main_frame_view import MainFrameView
from core.models.gameOnePlayer import GameOnePlayer
from core.models.grid import Grid
from core.models.human_player import HumanPlayer


class MainController:

    def __init__(self, mainFrame):
        self.mainFrame = mainFrame
        self.view = MainFrameView(self.mainFrame, self)
        self.menu_controller = MenuController(self.mainFrame)
        self.game_controller = GameController(self.mainFrame, GameOnePlayer(Grid.grid_by_ten(),
                                                                            HumanPlayer(69, "test")))
        self.menu_controller.add_observer(self.game_controller)

    def run(self):
        self.mainFrame.mainloop()
