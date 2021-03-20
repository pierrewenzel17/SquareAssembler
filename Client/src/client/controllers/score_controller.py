from tkinter import StringVar

from client.views.score_view import ScoreView


class ScoreController:

    def __init__(self, parent) -> None:
        self.parent = parent
        self.var_score = StringVar(value='5')
        self.var_block_score = StringVar(value='5')
        self.view = ScoreView(parent, self)

    def __create_string_var(self):
        self.value = StringVar()
        self.value.set("0")
        return self.value

    def reloadScore(self):
        self.view.reload()