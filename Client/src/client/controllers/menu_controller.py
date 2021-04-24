from client.controllers.view_update import Observable
from client.views.menu_view import MenuView
from core.models.grid import Grid


class MenuController(Observable):

    def __init__(self, parent,player) -> None:
        self.player = player
        super().__init__()
        self.parent = parent
        self.view = MenuView(parent, self)

    def new_game(self, grid):

            super().notify(self.gride_creator(grid))

    def gride_creator(self,val:int):
        return Grid.grid_by_ten() if val ==1 else Grid.grid_by_twenty()

    def new_game_online(self,grid,iserveur):
        super().notify_online(grid,iserveur)

