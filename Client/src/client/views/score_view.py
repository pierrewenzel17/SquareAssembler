from tkinter import Frame, Label, TOP

from client.views import fontstyle


class ScoreView(Frame):

    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.grid(row=1, column=2, ipadx=50, sticky="NEWS")

        self.lb_score = Label(self, text="Score", background="white", font=("Courier", 25)).pack(side=TOP)
        self.scorePrinting = Label(self, textvariable=self.controller.var_score.get(), font=fontstyle.scoreFont())\
            .pack()

        self.lb_block_score = Label(self, text="Block Score", background="white", font=("Courier", 25)).pack(side=TOP)
        self.scoreBlockPrinting = Label(self, textvariable=self.controller.var_block_score.get(), font=fontstyle.scoreFont())\
            .pack()

    def reload(self):
        pass