from tkinter import Frame, Canvas, BOTH

from core.models import Grid


class GridView(Frame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=1, rowspan=2, ipadx=300, ipady=300, sticky="NEWS")
        self.print_grid(Grid.grid_by_ten())

    def print_grid(self, grid):
        self.clear_grid()

        canvas = Canvas(self, width=0, height=0)
        canvas.pack(fill=BOTH, expand=1)
        rectangleSize = 600 / grid.nb_col_row
        for i in range(0, grid.nb_col_row):
            for j in range(0, grid.nb_col_row):
                canvas.create_rectangle(i * rectangleSize, j * rectangleSize, rectangleSize * (i+1),
                                        rectangleSize * (j+1), fill=grid[i, j].color.value)

    def clear_grid(self):
        for widget in self.winfo_children():
            widget.destroy()
