from tkinter import Tk

from client.controllers.end_controleur import EndController
from client.controllers.game_controller import GameController
from client.controllers.menu_controller import MenuController
from core.models.gameOnePlayer import GameOnePlayer

import client.controllers.online_controlleur as oc

from client.controllers.view_update import Observer
from client.utils.constant_util import Constants

from client.views.main_frame_view import MainFrameView

from core.models.human_player import HumanPlayer


class MainController(Observer):

    def __init__(self, mainFrame, grid):
        self.mainFrame = mainFrame
        self.player = HumanPlayer(69, "test")
        self.view = MainFrameView(self.mainFrame, self)
        self.menu_controller = MenuController(self.mainFrame, self.player)
        game=GameOnePlayer(grid)
        game.set_player(self.player)
        self.game_controller = GameController(self.mainFrame,game)
        self.menu_controller.add_observer(self)
        end_vcontroleur=EndController()
        end_vcontroleur.add_observer(self)
        self.game_controller.set_end_controller(end_vcontroleur)
        self.__main_job=None

    def run(self):
        self.update_time()
        self.refresh_view()
        self.__main_job = self.mainFrame.mainloop()

    def update_time(self):
        self.game_controller.up_timer()

        self.__jobtime = self.mainFrame.after(1000, self.update_time)

    def refresh_view(self):
        self.game_controller.grd_refresh()
        self.__jobrefresh = self.mainFrame.after(100, self.refresh_view)

    def update(self, data) -> None:
        self.__stop()
        endcontrolleur=self.game_controller.end_controlleur

        self.game_controller=GameController(self.mainFrame,GameOnePlayer(data))
        self.game_controller.game.set_player(self.player)
        self.game_controller.set_end_controller(endcontrolleur)
        self.refresh_view()
        self.update_time()

    def update_obline(self, data, iserveur) -> None:

        self.__stop()
        controller_main = oc.OnlineControlleur(iserveur, data)
        controller_main.add_apelant(self)
        controller_main.online_game()

    def craft_game(self, controleur):
        endcontrolleur = self.game_controller.end_controlleur
        self.game_controller =controleur

        self.game_controller.adapt(self.mainFrame)
        self.game_controller.game.set_player(self.player)
        self.game_controller.set_end_controller(endcontrolleur)
        self.refresh_view()

        self.update_time()

    def update_quit(self):
        self.__stop()
        self.mainFrame.quit()
        self.mainFrame.destroy()

    def __stop(self):
        if self.__jobtime is not None:
            self.mainFrame.after_cancel(self.__jobtime)
            self.__jobtime = None
        if self.__jobrefresh is not None:
            self.mainFrame.after_cancel(self.__jobrefresh)
            self.__jobrefresh = None
        self.game_controller.quit()