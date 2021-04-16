from threading import Timer

from tkinter import Tk

from client.controllers.main_online_controller import MainOnlineController
from client.models.serveur import StateOnline, MyAgent
from client.utils.constant_util import Constants

from core.models.grid import Grid
from core.models.position import Position


class OnlineControlleur:

    def __init__(self, state_online, type_game: int):

        self.agent = MyAgent("my_agent", state_online)
        self.game_controlleur = None
        self.is_alone = True
        self.state_online = state_online
        self.my_turn = True if self.state_online == StateOnline.JOIN else False
        # controleur gérant la connection entre l'Ivy le back et le front
        self.superieur = None
        self.typegame = type_game

    def online_game(self):
        print("on lance l'Ivy")

        def connect(agent, status):
            print("boubou")
            grid: Grid
            if self.typegame == 1:
                grid = Grid.grid_by_ten()
            else:
                grid = Grid.grid_by_twenty()
            if self.is_alone:
                self.is_alone = False
                if status == StateOnline.JOIN.name and self.state_online == StateOnline.CREATE:
                    # create grid voir avec Cyril
                    # On evoie la grille
                    self.agent.send_msg(f'grid={grid.__str__()}')
                    print("la grille créé")
                    print(grid.__str__())
                    self.change_to_game(grid)
                elif status == StateOnline.CREATE.name and self.state_online == StateOnline.JOIN:
                    self.agent.send_msg(f'connect={StateOnline.JOIN.name}')

                # paramétrer le changement de vue
                # crée un controlleur gamme online reliant ala foi les view_ grid et la wiew score.
                # + linkage du oneline controlleur

        def load_grid(agent, grid):
            # On charge la grille coté client voir avec cyril
            print("La grid reçu est : " + grid)
            gride: Grid = Grid.rebulde(grid)
            self.change_to_game(gride)

        def play(agent, position):
            # voir avec cyril fonction qui represente le coup de l'adversaire
            # reception du coup
            # supperssion des cube
            print("ouiiiiii")
            self.game_controlleur.coup_adverse(position)
            self.my_turn = True

        self.agent.bind_msg(connect, f'connect=({StateOnline.CREATE.name}|{StateOnline.JOIN.name})')
       # self.agent.bind_msg(play_little_game, f'pos=(.*)')
        self.agent.bind_msg(play, f'i=(.*)')

        if self.state_online == StateOnline.JOIN:
            self.agent.bind_msg(load_grid, f'grid=(.*)')

        Timer(2.0, lambda: self.agent.start()).start()
        # sleep(3)
        # self.agent.start()
        # print(self.agent.get_subscriptions())

    def turn_click(self, position: Position):
        # voir avec Cyril
        if self.my_turn:
            print(position)
            # test sur si la couleur est disponible ; suppersion des cube de la met envoyer le cube clicker a l'autre
            print(self.agent.send_msg(f'pos={position.__str__()}'))
            self.my_turn = False

    def rollback(self):
        if self.agent is not None:
            self.agent.stop()

    def change_to_game(self, grid):

        print(grid.nb_col_row)
        # fonction permetant de passé de l'ecran de recherche de gamme à l'ecrtan de jeu

        mainFrame = Tk()
        mainFrame.title(Constants.GAME_TITLE)
        mainFrame.resizable(width=Constants.RESIZE_FRAME, height=Constants.RESIZE_FRAME)
        mainFrame.minsize(Constants.FRAME_WIDTH, Constants.FRAME_HEIGHT)

        controller_main = MainOnlineController(mainFrame, grid, self)
        self.game_controlleur = controller_main
        controller_main.run()
