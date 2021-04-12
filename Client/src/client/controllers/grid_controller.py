from client.controllers.view_update import Observable
from client.views.grid_view import GridView
from core.models.grid import Grid
from core.models.position import Position


class GridController(Observable):
    def __init__(self, parent, game_controller):
        super().__init__()
        self.game_controller = game_controller
        self.parent = parent
        self.view = GridView(self.parent, self)

    def printgrid(self) -> None:
        self.view.print_grid(self.game_controller.game.board,self.game_controller.game.CubeArray)

    def onClickEvent(self, event) -> None:
        self.game_controller.game.play()
        self.game_controller.score_controller.var_score.set(self.game_controller.game.getscore())
        self.onHoveringEvent(event)
        if self.game_controller.game.isclear():
            self.game_controller.game.player.save_score()
            self.view.end_view()

    def onHoveringEvent(self, event):
        self.game_controller.game.move(self.__getCubeByCoord(event))
        self.printgrid()
        self.game_controller.score_controller.var_block_score.set(len(self.game_controller.game.CubeArray))

    def __getCubeByCoord(self, event):
        return Position(convertWorldToGrid(event.y, self.game_controller.game.board.nb_col_row),
                        convertWorldToGrid(event.x, self.game_controller.game.board.nb_col_row))

    def new_game(self, grid):
        if grid == 1:
            super().notify(Grid.grid_by_ten())
        else:
            super().notify(Grid.grid_by_twenty())

    def update(self,valeur):
        if valeur==1:
            self.game_controller.update(Grid.grid_by_ten())
        else :
            self.game_controller.update(Grid.grid_by_twenty())

def convertWorldToGrid(y, nbcolunn):
    cubeSize = 600 / nbcolunn
    x = int(y / cubeSize)
    if x > nbcolunn - 1:
        x = nbcolunn - 1
    return x
