from client.controllers.game_controller import GameController
from core.models.position import Position


class Game_Online_contolleur(GameController):

    def __init__(self, parent, game, OnlineControlleur):
        GameController.__init__(self, parent, game)
        self.online_controleur = OnlineControlleur

    def coup_adverse(self, position):
        pos = Position.rebuld(position)
        self.game.changeTurn(self.online_controleur.my_turn)
        self.game.move(pos)
        self.game.play()
        self.online_controleur.my_turn = True

    def grid_effect(self, event):
        if self.game.coup_valide() and self.online_controleur.my_turn:
            self.game.changeTurn(self.online_controleur.my_turn)
            self.online_controleur.turn_click(self.game.CubeArray[0])
            GameController.grid_effect(self, event)
