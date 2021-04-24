from threading import Timer


from client.controllers.Play_online_xontrolleur import play_controlleur

from client.controllers.game_online_controlleur import Game_Online_contolleur

from client.models.serveur import StateOnline, MyAgent

from core.models.gameTwoPlayer import GameTwoPlayer

from core.models.grid import Grid


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
        self.control=None

    def add_apelant(self, invoc):
        self.invoc = invoc

    def online_game(self):

        def connect(agent, status):

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

                    self.change_to_game(grid)
                elif status == StateOnline.CREATE.name and self.state_online == StateOnline.JOIN:
                    self.agent.send_msg(f'connect={StateOnline.JOIN.name}')

                # paramétrer le changement de vue
                # crée un controlleur gamme online reliant ala foi les view_ grid et la wiew score.
                # + linkage du oneline controlleur

        def load_grid(agent, grid):
            # On charge la grille coté client voir avec cyril

            gride: Grid = Grid.rebulde(grid)
            self.change_to_game(gride)

        self.agent.bind_msg(connect, f'connect=({StateOnline.CREATE.name}|{StateOnline.JOIN.name})')
        # self.agent.bind_msg(play_little_game, f'pos=(.*)')

        if self.state_online == StateOnline.JOIN:
            self.agent.bind_msg(load_grid, f'grid=(.*)')

        Timer(2.0, lambda: self.agent.start()).start()
        # sleep(3)
        # self.agent.start()
        # print(self.agent.get_subscriptions())

    def rollback(self):
        if self.agent is not None:
            self.agent.stop()

    def change_to_game(self, grid):
        self.agent.stop()
        self.agent = None
        game = GameTwoPlayer(grid, 10)
        con = Game_Online_contolleur(None, game, play_controlleur(self.state_online, self.my_turn))

        self.invoc.craft_game(con)

    def onlinec_game(self):

        def connect(agent, status):

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

                    self.change_to_gamec(grid)
                elif status == StateOnline.CREATE.name and self.state_online == StateOnline.JOIN:
                    self.agent.send_msg(f'connect={StateOnline.JOIN.name}')

                # paramétrer le changement de vue
                # crée un controlleur gamme online reliant ala foi les view_ grid et la wiew score.
                # + linkage du oneline controlleur

        def load_grid(agent, grid):
            # On charge la grille coté client voir avec cyril

            gride: Grid = Grid.rebulde(grid)
            self.change_to_gamec(gride)

        self.agent.bind_msg(connect, f'connect=({StateOnline.CREATE.name}|{StateOnline.JOIN.name})')
        # self.agent.bind_msg(play_little_game, f'pos=(.*)')

        if self.state_online == StateOnline.JOIN:
            self.agent.bind_msg(load_grid, f'grid=(.*)')

        Timer(2.0, lambda: self.agent.start()).start()
        # sleep(3)
        # self.agent.start()
        # print(self.agent.get_subscriptions())

    def change_to_gamec(self, grid):
        self.agent.stop()
        self.agent = None
        game = GameTwoPlayer(grid, 10)


        con = Game_Online_contolleur(None, game, play_controlleur(self.state_online, self.my_turn))
        self.control=con
