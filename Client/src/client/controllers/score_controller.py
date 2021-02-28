from tkinter import StringVar

from client.controllers.view_update import Observable, Observer
from client.views.score_view import ScoreView


class ScoreController:

    def __init__(self, parent) -> None:
        self.parent = parent
        self.var_score = self.__create_string_var()
        self.var_block_score = self.__create_string_var()
        self.view = ScoreView(parent, self)

    def __create_string_var(self):
        value = StringVar()
        value.set("0")
        return value


""" def update_label_score(self):
        # self.view.scorePrinting["text"] = self.var_score.get()
        pass

    def update_label_block_score(self):
        # TODO
        pass
"""
