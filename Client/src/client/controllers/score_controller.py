from tkinter import IntVar, StringVar

from client.views.score_view import ScoreView


class ScoreController:

    def __init__(self, parent) -> None:
        self.parent = parent
        self.var_score = IntVar(value=0)
        self.var_block_score = IntVar(value=0)
        self.var_time = StringVar(value="")
        self.view = ScoreView(parent, self)


    def reload_color(self,color):
        self.view.contruct_kist_of_cole(color)

    def upfdate_timer(self,time):
        self.var_time.set("time : "+str(time))