from client.controllers.grid_controller import GridController
from client.controllers.menu_controller import MenuController
from client.controllers.score_controller import ScoreController
from client.views.main_frame_view import MainFrameView


class MainController:

    def __init__(self, root):
        self.parent = root
        self.view = MainFrameView(self.parent, self)
        self.grid_controller = GridController(self.parent)
        self.score_controller = ScoreController(self.parent)
        self.menu_controller = MenuController(self.parent)
        self.menu_controller.add_observer(self.grid_controller)

    def run(self):
        self.parent.mainloop()


