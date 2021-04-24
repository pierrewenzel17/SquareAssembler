from tkinter import Frame, Canvas, BOTH, Toplevel, IntVar, Label, Radiobutton, Button, CENTER, TOP


from core.models.position import Position


class GridView(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=1, rowspan=2, ipadx=300, ipady=300, sticky="NEWS")
        self.canvas:Canvas =Canvas(self, width=0, height=0, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=1)

    def print_grid(self, grid, liste):
        self.canvas.delete('all')

        cubeSize = 600 / grid.nb_col_row

        for i in range(0, grid.nb_col_row):
            for j in range(0, grid.nb_col_row):
                if grid[i, j] is not None:
                    vecteur = Position(i, j)
                    if vecteur in liste:
                        self.canvas.create_rectangle(j * cubeSize, i * cubeSize, cubeSize * (j + 1),
                                                cubeSize * (i + 1), fill=grid[i, j].color.value, stipple="gray50"
                                                )
                    else:
                        self.canvas.create_rectangle(j * cubeSize, i * cubeSize, cubeSize * (j + 1),
                                                cubeSize * (i + 1), fill=grid[i, j].color.value)
        self.canvas.bind("<Button-1>", self.controller.onClickEvent)
        self.canvas.bind("<Motion>", self.controller.onHoveringEvent)



