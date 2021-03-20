from tkinter import StringVar

from client.views.score_view import ScoreView


class ScoreController:

    def __init__(self, parent) -> None:
        self.parent = parent
        self.var_score = self.__create_string_var()
        self.var_block_score = self.__create_string_var()
        self.view = ScoreView(parent, self)

    def __create_string_var(self):
        self.value = StringVar()
        self.value.set("0")
        return self.value
