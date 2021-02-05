from tkinter import Frame, Canvas, S, N, E, W

from core.models import Grid


class GridView(Frame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid(row=0, column=1, rowspan=2, ipadx=400, ipady=400, sticky="NEWS")
        self.print_grid(Grid.grid_by_twenty())

    def print_grid(self, grid):
        # self.option_clear()
        for i in range(0, grid.nb_col_row):
            self.rowconfigure(i, weight=1)
            for j in range(0, grid.nb_col_row):
                self.columnconfigure(j, weight=1)
                Canvas(self, bg=grid[i, j].color.value, width=self.winfo_width(), height=self.winfo_height()).grid(
                    row=i, column=j, sticky=S + N + E + W)
