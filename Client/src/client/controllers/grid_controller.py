from client.controllers import Observer
from client.views import GridView


class GridController(Observer):
    def __init__(self, parent):
        self.parent = parent
        self.view = GridView(self.parent, self)

    def update(self, grid) -> None:
        for widget in self.view.winfo_children():
            widget.destroy()
        self.view.print_grid(grid)
