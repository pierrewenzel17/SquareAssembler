from client.controllers.game_online_controlleur import Game_Online_contolleur
from client.controllers.menu_controller import MenuController
from client.views.main_frame_view import MainFrameView
from core.models.gameTwoPlayer import GameTwoPlayer

from core.models.human_player import HumanPlayer


class MainOnlineController:

    def __init__(self, mainFrame, grid,onlinecontroller ):
        self.mainFrame = mainFrame
        player = HumanPlayer(69, "test")
        self.view = MainFrameView(self.mainFrame, self)
        self.menu_controller = MenuController(self.mainFrame, player)
        self.game_controller = Game_Online_contolleur(self.mainFrame, GameTwoPlayer(grid,
                                                                            player,10),onlinecontroller)
        self.menu_controller.add_observer(self.game_controller)

    def run(self):
        self.mainFrame.mainloop()
