from tkinter import Frame, Canvas, BOTH, Toplevel, IntVar, Label, Radiobutton, Button, CENTER, TOP


from core.models.position import Position


class GridView(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
##        self.onlineController = OnlineControlleur()
        self.grid(row=0, column=1, rowspan=2, ipadx=300, ipady=300, sticky="NEWS")

    def print_grid(self, grid, liste):
        self.clear_grid()
        cubeSize = 600 / grid.nb_col_row
        canvas = Canvas(self, width=0, height=0, borderwidth=0, highlightthickness=0)
        canvas.pack(fill=BOTH, expand=1)
        for i in range(0, grid.nb_col_row):
            for j in range(0, grid.nb_col_row):
                if grid[i, j] is not None:
                    vecteur = Position(i, j)
                    if vecteur in liste:
                        canvas.create_rectangle(j * cubeSize, i * cubeSize, cubeSize * (j + 1),
                                                cubeSize * (i + 1), fill=grid[i, j].color.value, stipple="gray50"
                                                )
                    else:
                        canvas.create_rectangle(j * cubeSize, i * cubeSize, cubeSize * (j + 1),
                                                cubeSize * (i + 1), fill=grid[i, j].color.value)
        canvas.bind("<Button-1>", self.controller.onClickEvent)
        canvas.bind("<Motion>", self.controller.onHoveringEvent)

    def clear_grid(self):
        for widget in self.winfo_children():
            widget.destroy()

    def end_view(self):
        top = Toplevel()
        top.title("Relancer une nouvelle partie")
        top.geometry("300x200+550+350")
        top.minsize(300, 200)
        radio_var = IntVar()
        radio_var.set(1)

        Label(top, text="Partie terminée !", font=("Courier", 20, "bold")).pack(side=TOP)
        Radiobutton(top, text="grille 10x10", variable=radio_var, value=1, relief='solid') \
            .place(relx=0.3, rely=0.3, anchor=CENTER)
        Radiobutton(top, text="grille 20x20", variable=radio_var, value=2, relief='solid') \
            .place(relx=0.7, rely=0.3, anchor=CENTER)
        Button(top, text="Jouer seul", width=30, relief='solid',
               command=lambda: [self.resetlocal(radio_var.get()), top.destroy()]) \
            .place(relx=0.5, rely=0.5, anchor=CENTER)

        top.mainloop()
        '''
        Button(top, text="Créer une partie en ligne", width=30, relief='solid',
               command=lambda: self.onlineController.create_game(OnlineView())) \
            .place(relx=0.5, rely=0.7, anchor=CENTER)
        Button(top, text="Rejoindre une partie en ligne", width=30, relief='solid',
               command=lambda: self.onlineController.join_game(OnlineView())) \
            .place(relx=0.5, rely=0.9, anchor=CENTER)
        '''
    def resetlocal(self,val):

        self.controller.update(val)