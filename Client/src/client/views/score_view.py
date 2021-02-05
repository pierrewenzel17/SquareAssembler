from tkinter import Frame, Label, TOP


class ScoreView(Frame):

    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.grid(row=1, column=2, ipadx=100, ipady=175, sticky="NEWS")
        self.lb_titre = Label(self, text="Score", background="white", font=("Courier", 25)).pack(side=TOP)
