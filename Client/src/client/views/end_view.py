from tkinter import Button,  Toplevel, IntVar, Label, Radiobutton, CENTER, TOP

from client.models.serveur import StateOnline


class End_view:
    def __init__(self,controleur):
        self.controller=controleur

    def newGameChoiceFrame(self):
        top = Toplevel()
        top.title("Choisir nouveau jeu")
        top.minsize(300, 200)
        radio_var = IntVar()
        radio_var.set(1)

        Label(top, text="Menu", font=("Courier", 25, "bold")).pack(side=TOP)
        Radiobutton(top, text="grille 10x10", variable=radio_var, value=1, relief='solid') \
            .place(relx=0.3, rely=0.3, anchor=CENTER)
        Radiobutton(top, text="grille 20x20", variable=radio_var, value=2, relief='solid') \
            .place(relx=0.7, rely=0.3, anchor=CENTER)
        Button(top, text="Jouer seul", width=30, relief='solid',
               command=lambda: [top.destroy(), self.controller.new_game(radio_var.get())]) \
            .place(relx=0.5, rely=0.5, anchor=CENTER)
        Button(top, text="Créer une partie en ligne", width=30, relief='solid',
               command=lambda: [top.destroy(), self.controller.new_game_online(radio_var.get(), StateOnline.CREATE)]) \
            .place(relx=0.5, rely=0.7, anchor=CENTER)
        Button(top, text="Rejoindre une partie en ligne", width=30, relief='solid',
               command=lambda: [top.destroy(), self.controller.new_game_online(radio_var.get(), StateOnline.JOIN)]) \
            .place(relx=0.5, rely=0.9, anchor=CENTER)

        top.mainloop()
