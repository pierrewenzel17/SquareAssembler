from client.controllers.view_update import Observer
from client.views.grid_view import GridView


class GridController(Observer):
    def __init__(self, parent):
        self.parent = parent
        self.view = GridView(self.parent, self)

    def update(self, grid) -> None:
        self.view.print_grid(grid)
