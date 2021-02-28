from tkinter import Frame, Canvas, BOTH

from core.models.grid import Grid


class GridView(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=1, rowspan=2, ipadx=300, ipady=300, sticky="NEWS")


    def print_grid(self, grid):
        self.clear_grid()
        cubeSize = 600 / grid.nb_col_row
        canvas = Canvas(self, width=0, height=0)
        canvas.pack(fill=BOTH, expand=1)
        for i in range(0, grid.nb_col_row):
            for j in range(0, grid.nb_col_row):
                canvas.create_rectangle(i * cubeSize, j * cubeSize, cubeSize * (i + 1),
                                        cubeSize * (j + 1), fill=grid[i, j].color.value)
        # canvas.bind("<Button-1>", self.controller.onClickEvent)
        # canvas.bind("<Motion>", self.controller.onHoveringEvent)

    def clear_grid(self):
        for widget in self.winfo_children():
            widget.destroy()
