from client.controllers.view_update import Observable
from client.views.end_view import End_view

from core.models.grid import Grid


class EndController(Observable):

    def __init__(self) -> None:

        super().__init__()

        self.view = End_view( self)

    def new_game(self, grid):

            super().notify(self.gride_creator(grid))

    def gride_creator(self,val:int):
        return Grid.grid_by_ten() if val ==1 else Grid.grid_by_twenty()

    def new_game_online(self,grid,iserveur):
        super().notify_online(grid,iserveur)

    def print_end(self):
        self.view.newGameChoiceFrame()