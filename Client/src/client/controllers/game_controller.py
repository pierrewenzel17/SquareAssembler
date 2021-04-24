from client.controllers.grid_controller import GridController

from client.controllers.score_controller import ScoreController



class GameController:

    def __init__(self, parent, game):
        self.game = game
        if parent is not None :
            self.grid_controller = GridController(parent, self)
            #self.grid_controller.printgrid()
            self.score_controller = ScoreController(parent)
            self.score_controller.reload_color(self.game.get_player_color())
        self.end_controlleur=None

    def react_click(self, event):
        self.grid_effect(event)
        self.scor_effect()
        self.end_impact()

    def grd_refresh(self):
        self.grid_controller.printgrid()

    def grid_effect(self,event):
        self.game.play()
        self.grid_controller.onHoveringEvent(event)

    def scor_effect(self):
        self.score_controller.var_score.set(self.game.getscore())

    def end_impact(self):
        if self.game.isclear():
            self.game.game_master().save_score()
            self.end_controlleur.print_end()

    def on_hovering_effect(self,position):
        self.game.move(position)

    def adapt(self, parent):
        self.parent = parent
        self.grid_controller = GridController(parent, self)

        self.score_controller = ScoreController(parent)
        self.score_controller.reload_color(self.game.get_player_color())


    def up_timer(self):
        pass

    def quit(self):
        print("p")

    def set_end_controller(self, end_vcontroleur):
        self.end_controlleur=end_vcontroleur