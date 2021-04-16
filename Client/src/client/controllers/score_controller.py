from tkinter import IntVar

from client.views.score_view import ScoreView


class ScoreController:

    def __init__(self, parent) -> None:
        self.parent = parent
        self.var_score = IntVar(value=0)
        self.var_block_score = IntVar(value=0)
        self.view = ScoreView(parent, self)

    def reload_color(self):
        pass