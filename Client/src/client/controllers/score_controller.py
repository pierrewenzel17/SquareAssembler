from tkinter import StringVar

from client.controllers.view_update import Observable, Observer
from client.views.score_view import ScoreView


class ScoreController(Observer):

    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.var_score = self.__create_string_var(self.update_label_score())
        self.var_block_score = self.__create_string_var(self.update_label_block_score())
        self.view = ScoreView(parent, self)

    def __create_string_var(self, observer):
        value = StringVar()
        value.set("0")
        value.trace("w", observer)
        return value

    def update_label_score(self):
        # TODO
        pass

    def update_label_block_score(self):
        # TODO
        pass
