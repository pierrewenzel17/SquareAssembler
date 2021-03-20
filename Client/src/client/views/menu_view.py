from tkinter import Frame, Button, Menu, Toplevel, messagebox, IntVar, Label, Radiobutton, Checkbutton, BOTTOM, TOP


def about():
    messagebox.showinfo("Information", "Made by \n\n BURTIN Cyril \n WENZEL Pierre \n PHILIPP Sebastien ")


class MenuView(Frame):

    def __init__(self, master, controller):
        super().__init__(master, background="white")
        self.controller = controller

        self.menuBar = Menu(master)
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Nouveau", command=lambda: self.newGameChoiceFrame())
        self.fileMenu.add_command(label="Quitter", command=master.quit)
        self.menuBar.add_cascade(label="Jeu", menu=self.fileMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="Aide", command=lambda: about())
        self.menuBar.add_cascade(label="A propos", menu=self.helpMenu)

        master.config(menu=self.menuBar)

    def newGameChoiceFrame(self):
        top = Toplevel()
        top.title("Choisir nouveau jeu")
        top.minsize(300, 150)
        radio_var = IntVar()
        online_var = IntVar()
        Label(top, text="Menu", background="white", font=("Courier", 25)).pack(side=TOP)
        Radiobutton(top, text="Grille de 100 cube", variable=radio_var, value=1,
                    font=("Courier", 12)).pack()
        Radiobutton(top, text="Grille de 400 cube", variable=radio_var, value=2,
                    font=("Courier", 12)).pack()
        Checkbutton(top, text="Partie en ligne", variable=online_var, font=("Courier", 12)).pack()
        Button(top, text="Recommencer la partie", font=("Courier", 12),
               command=lambda: [self.controller.new_game(radio_var.get(), online_var.get()),
                                top.destroy()]).pack(side=BOTTOM)

        top.mainloop()
