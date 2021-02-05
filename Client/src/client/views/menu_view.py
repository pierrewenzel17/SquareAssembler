from tkinter import Frame, Tk, Button, Label, TOP, BOTTOM, Radiobutton, Checkbutton, IntVar


class MenuView(Frame):

    def __init__(self, master, controller):
        super().__init__(master, background="white")
        self.controller = controller
        self.grid(row=0, column=2, ipadx=100, ipady=140, sticky="EW")
        radio_var = IntVar()
        online_var = IntVar()
        self.lb_titre = Label(self, text="Menu", background="white", font=("Courier", 25)).pack(side=TOP)
        self.btn_Grid_100 = Radiobutton(self, text="Grille de 100 cube", variable=radio_var, value=1,
                                        font=("Courier", 12)).pack()
        self.btn_Grid_400 = Radiobutton(self, text="Grille de 400 cube", variable=radio_var, value=2,
                                        font=("Courier", 12)).pack()
        self.btn_online = Checkbutton(self, text="Partie en ligne", variable=online_var, font=("Courier", 12)).pack()
        self.btn_restart = Button(self,
                                  text="Recommencer la partie",
                                  font=("Courier", 12),
                                  command=lambda: self.controller.new_game(radio_var.get(), online_var.get())).pack(
            side=BOTTOM)
