from client.controllers.view_update import Observer
from client.views.grid_view import GridView
from core.models.grid import Grid
from core.models.position import Position


class GridController:
    def __init__(self, parent, game_controller):
        self.game_controller = game_controller
        self.parent = parent
        self.view = GridView(self.parent, self)

    def printgrid(self) -> None:
        self.view.print_grid(self.game_controller.game.board)

    def onClickEvent(self, event) -> None:

        """ réfléchir à l'enventualité de remonter le code dans la classe game_controlleur """
        if len(self.game_controller.game.CubeArray)>2:
            self.game_controller.game.play()
            self.printgrid()

            self.game_controller.score_controller.var_score.set(self.game_controller.game.getscore())
            self.onHoveringEvent(event)
            if self.game_controller.game.isclear():
                self.game_controller.game.player.save_score()
                self.view.endView()

    def onHoveringEvent(self, event):
        self.game_controller.game.move(self.__getCubeByCoord(event))
        self.view.changeColorForme(self.game_controller.game.CubeArray)
        self.game_controller.score_controller.var_block_score.set(len(self.game_controller.game.CubeArray))
    def __getCubeByCoord(self, event):

        return Position(convertWorldToGrid(event.y, self.game_controller.game.board.nb_col_row),
                        convertWorldToGrid(event.x, self.game_controller.game.board.nb_col_row))


def convertWorldToGrid(y, nbcolunn):
    cubeSize = 600 / nbcolunn
    x = int(y / cubeSize)
    if x > nbcolunn - 1:
        x = nbcolunn - 1
    return x
