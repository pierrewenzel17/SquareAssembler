from client.controllers.game_controller import GameController

from client.utils.constant_util import Constants
from core.models.position import Position


class Game_Online_contolleur(GameController):

    def __init__(self, parent, game, OnlineControlleur):
        GameController.__init__(self, parent, game)
        self.online_controleur = OnlineControlleur
        OnlineControlleur.game_controlleur=self
        self.online_controleur.exodia()
        self.time = self.game.get_time()
        if not self.online_controleur.my_turn and parent is not None :
            self.score_controller.var_time.set(Constants.MESSAGE_ADVERCE_TURN)

    def coup_adverse(self, position):
        pos = Position.rebuld(position)
        self.game.changeTurn(self.online_controleur.my_turn)
        self.game.move(pos)
        self.game.play()
        self.pass_to_my_turn()
        self.score_controller.reload_color(self.game.get_player_color())
        self.end_impact()
        if not self.game.playercanplay() :

            self.online_controleur.agent.send_msg("no")
            self.pas_to_other_turn()

    def grid_effect(self, event):
        if self.game.coup_valide() and self.online_controleur.my_turn:
            self.game.changeTurn(self.online_controleur.my_turn)

            self.online_controleur.turn_click(self.game.CubeArray[0])
            GameController.grid_effect(self, event)
            self.score_controller.reload_color(self.game.get_player_color())
            self.pas_to_other_turn()

    def up_timer(self):

        if self.online_controleur.my_turn:
            self.score_controller.upfdate_timer(self.time)
            if self.time == 0:
                self.online_controleur.agent.send_msg("no")
                self.pas_to_other_turn()
            self.time -= 1



    def pass_to_my_turn(self):
        self.online_controleur.my_turn = True
        self.game.changeTurn(self.online_controleur.my_turn)
        self.time = self.game.get_time()
        self.game.reset_cube_array()



    def pas_to_other_turn(self):
        self.online_controleur.my_turn = False
        self.game.changeTurn(self.online_controleur.my_turn)
        self.score_controller.var_time.set(Constants.MESSAGE_ADVERCE_TURN)
        self.game.reset_cube_array()

    def on_hovering_effect(self, position):
        if self.online_controleur.my_turn:
            GameController.on_hovering_effect(self, position)

    def adapt(self, parent):
        GameController.adapt(self,parent)
        if not self.online_controleur.my_turn:
            self.score_controller.var_time.set(Constants.MESSAGE_ADVERCE_TURN)

    def quit(self):
        self.online_controleur.agent.send_msg('parti')
        self.online_controleur.agent.stop()
        self.online_controleur.agent=None
    def grd_refresh(self):

        GameController.grd_refresh(self)