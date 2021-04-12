from tkinter import Frame, Label, Canvas, BOTH

from client.views import fontstyle


class ScoreView(Frame):

    def __init__(self, master, controller) -> None:
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=2, pady=50, sticky="NEWS")
        self.lb_score = Label(self, text="Score", font=("Courier", 25)).pack()
        self.scorePrinting = Label(self, textvariable=self.controller.var_score, font=fontstyle.scoreFont()).pack()
        self.lb_block_score = Label(self, text="Bloc Score", font=("Courier", 25)).pack()
        self.scoreBlockPrinting = Label(self, textvariable=self.controller.var_block_score, font=fontstyle.scoreFont())\
            .pack()

        COLORS = ["Red", "Green", "Blue", "Yellow", "Red", "Green", "Blue", "Yellow"]

        self.blank = Label(self, height=1).pack()
        self.color_dispo = Label(self, text="Couleurs disponible :", font=("Courier", 15)).pack()
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0 )
        self.canvas.pack(fill=BOTH, expand=1)
        for i in range(0, COLORS.__len__()):
            self.canvas.create_rectangle(100, i * 25, 150, 25 * (i + 1), fill=COLORS[i])
            self.canvas.create_text(200, i * 25 + 12.5, text=COLORS[i])
