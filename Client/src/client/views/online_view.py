from tkinter import Frame, Button, Label, BOTTOM, TOP, Tk

import client.controllers.online_controlleur as c


class OnlineView(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.controller = c.OnlineControlleur()
        self.label = Label(self, text="Recherche d'une partie en cours...", background="white",
                           font=("Courier", 25)).pack(side=TOP)
        self.btnCallback = Button(self, text="Annuler", font=("Courier", 12),
                                  command=lambda: self.controller.rollback(self)).pack(side=BOTTOM)
