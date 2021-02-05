from client.controllers import Observable
from client.views import MenuView
from core.models import Grid


class MenuController(Observable):

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.view = MenuView(parent, self)

    def new_game(self, grid, online):
        if grid == 1:
            super().notify(Grid.grid_by_ten())
        else:
            super().notify(Grid.grid_by_twenty())

