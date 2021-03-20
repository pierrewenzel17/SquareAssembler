from tkinter import Frame, Label

from client.views import fontstyle


class ScoreView(Frame):

    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.grid(row=1, column=2, ipadx=50, sticky="NEWS")
        self.lb_score = Label(self, text="Score", background="white", font=("Courier", 25)).pack()
        self.scorePrinting = Label(self, textvariable=self.controller.var_score, font=fontstyle.scoreFont()).pack()
        self.lb_block_score = Label(self, text="Block Score", background="white", font=("Courier", 25)).pack()
        self.scoreBlockPrinting = Label(self, textvariable=self.controller.var_block_score, font=fontstyle.scoreFont())\
            .pack()
