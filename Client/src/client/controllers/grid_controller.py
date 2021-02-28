from client.controllers.view_update import Observer
from client.views.grid_view import GridView
from core.models.grid import Grid


class GridController:
    def __init__(self, parent):
        self.parent = parent
        self.view = GridView(self.parent, self)

    def printgrid(self, grid) -> None:
        self.view.print_grid(grid)
