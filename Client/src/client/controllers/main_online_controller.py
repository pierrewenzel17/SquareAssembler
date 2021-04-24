from client.controllers.game_online_controlleur import Game_Online_contolleur
import client.controllers.main_controller as mc
from tkinter import Tk
import client.controllers.online_controlleur as oc
from client.controllers.menu_controller import MenuController
from client.controllers.view_update import Observer
from client.utils.constant_util import Constants
from client.views.main_frame_view import MainFrameView
from core.models.gameTwoPlayer import GameTwoPlayer
from core.models.human_player import HumanPlayer


class MainOnlineController(Observer):

    def __init__(self, mainFrame, grid, onlinecontroller):

        self.mainFrame = mainFrame
        player = HumanPlayer(69, "test")
        self.view = MainFrameView(self.mainFrame, self)
        self.menu_controller = MenuController(self.mainFrame, player)
        game = GameTwoPlayer(grid, 10)
        game.set_player(player)
        self.game_controller = Game_Online_contolleur(self.mainFrame, game, onlinecontroller)
        self.menu_controller.add_observer(self)

    def run(self):
        self.update_time()
        self.refresh_view()
        self.__main_job=self.mainFrame.mainloop()

    def update_time(self):
        self.game_controller.up_timer()
        self.__jobtime = self.mainFrame.after(1000, self.update_time)

    def refresh_view(self):
        self.game_controller.grd_refresh()
        self.__jobrefresh = self.mainFrame.after(100, self.refresh_view)

    def update(self, data) -> None:
        # self.game_controller.quit()
        if self.__jobtime is not None:
            self.mainFrame.after_cancel(self.__jobtime)
            self.__jobtime = None
        if self.__jobrefresh is not None:
            self.mainFrame.after_cancel(self.__jobrefresh)
            self.__jobrefresh = None
        if self.game_controller.online_controleur.agent is not None:
            self.game_controller.quit()
        self.mainFrame.destroy()
        if self.__main_job is not None:
            self.__main_job = None
        mainFrame = Tk()
        mainFrame.title(Constants.GAME_TITLE)
        mainFrame.resizable(width=Constants.RESIZE_FRAME, height=Constants.RESIZE_FRAME)
        mainFrame.minsize(Constants.FRAME_WIDTH, Constants.FRAME_HEIGHT)

        controller_main = mc.MainController(mainFrame, data)
        controller_main.run()

    def update_obline(self, data, iserveur) -> None:

        if self.__jobtime is not None:
            self.mainFrame.after_cancel(self.__jobtime)
            self.__jobtime = None
        if self.__jobrefresh is not None:
            self.mainFrame.after_cancel(self.__jobrefresh)
            self.__jobrefresh = None
        if self.game_controller.online_controleur.agent is not None:
            self.game_controller.quit()
        self.mainFrame.destroy()
        if  self.__main_job is not None:
            self.__main_job =None
        controller_main = oc.OnlineControlleur(iserveur, data)
        controller_main.online_game()
