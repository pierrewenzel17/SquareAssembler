from client.controllers.view_update import Observable
from client.views.menu_view import MenuView
from core.models.grid import Grid


class MenuController(Observable):

    def __init__(self, parent) -> None:
       ## self.player = player
        super().__init__()
        self.parent = parent
        self.view = MenuView(parent, self)

    def new_game(self, grid, online):
        if grid == 1:
            super().notify(Grid.grid_by_ten())
        else:
            super().notify(Grid.grid_by_twenty())
