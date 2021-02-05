from client.controllers import GridController, MenuController, ScoreController
from client.views import MainFrameView


class MainController:

    def __init__(self, parent):
        self.parent = parent
        self.view = MainFrameView(parent, self)
        self.grid_controller = GridController(self.parent)
        self.menu_controller = MenuController(self.parent)
        self.score_controller = ScoreController(self.parent)
        self.menu_controller.add_observer(self.grid_controller)

    def run(self):
        self.parent.mainloop()


