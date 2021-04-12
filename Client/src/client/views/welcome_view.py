import os
from tkinter import PhotoImage, Canvas, Button, CENTER, NW, SW, Label, Tk, Radiobutton, IntVar

from client.controllers.main_controller import MainController
from client.controllers.online_controlleur import OnlineControlleur
from client.utils.constant_util import Constants
from client.views.online_view import OnlineView
from core.models.grid import Grid


class WelcomeView:
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root
        self.onlineController = OnlineControlleur()

        self.var = IntVar()
        self.var.set(1)
        self.bg = PhotoImage(file=os.path.join(os.getcwd(), 'resources/bg_image.gif'))
        self.canvas = Canvas(self.root, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.logo = PhotoImage(file=os.path.join(os.getcwd(), 'resources/logo.png'))
        self.canvas.create_image(300, 15, image=self.logo, anchor="n")
        self.radio_ten = Radiobutton(self.canvas, text="grille 10x10", variable=self.var, value=1,
                                     relief='solid', font=("Franklin Gothic Heavy", 12, "bold")) \
            .place(relx=0.35, rely=0.35, anchor=CENTER)
        self.radio_twenty = Radiobutton(self.canvas, text="grille 20x20", variable=self.var, value=2,
                                        relief='solid', font=("Franklin Gothic Heavy", 12, "bold")) \
            .place(relx=0.65, rely=0.35, anchor=CENTER)
        self.btnPlay = Button(self.canvas, text="Jouer seul", command=self.runGame, width=30, relief='solid',
                              font=("Franklin Gothic Heavy", 15, "bold")) \
            .place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btnCreateOnlineGame = Button(self.canvas, text="Créer une partie en ligne", width=30,
                                          font=("Franklin Gothic Heavy", 15, "bold"), relief='solid',
                                          command=lambda: self.onlineController.create_game(OnlineView())) \
            .place(relx=0.5, rely=0.6, anchor=CENTER)
        self.btnJoinOnlineGame = Button(self.canvas, text="Rejoindre une partie en ligne", width=30,
                                        font=("Franklin Gothic Heavy", 15, "bold"), relief='solid',
                                        command=lambda: self.onlineController.join_game(OnlineView())) \
            .place(relx=0.5, rely=0.7, anchor=CENTER)
        self.btnQuit = Button(self.canvas, text="Quitter", font=("Franklin Gothic Heavy", 15, "bold"), relief='solid',
                              command=self.root.quit) \
            .place(relx=0.5, rely=0.85, anchor=CENTER)

        self.createdBy = Label(self.canvas, text="Développé par BURTIN Cyril, WENZEL Pierre et PHILIPP Sebastien",
                               font=("Courier", 10), bg="lightgrey") \
            .place(relx=0, rely=1, anchor=SW, relwidth=1.0)

        self.canvas.create_window(10, 10, anchor=NW, window=self.btnPlay)
        self.canvas.create_window(10, 10, anchor=NW, window=self.btnQuit)
        self.canvas.create_window(10, 10, anchor=NW, window=self.createdBy)

    def runGame(self):
        self.root.destroy()
        mainFrame = Tk()
        mainFrame.title(Constants.GAME_TITLE)
        mainFrame.resizable(width=Constants.RESIZE_FRAME, height=Constants.RESIZE_FRAME)
        mainFrame.minsize(Constants.FRAME_WIDTH, Constants.FRAME_HEIGHT)
        print(self.var.get())
        if self.var.get() == 2:
            controller_main = MainController(mainFrame, Grid.grid_by_twenty())
        else:
            controller_main = MainController(mainFrame, Grid.grid_by_ten())
        controller_main.run()

    def run_online(self):
        self.root.destroy()
        mainFrame = Tk()
        mainFrame.title(Constants.GAME_TITLE)
        mainFrame.resizable(width=Constants.RESIZE_FRAME, height=Constants.RESIZE_FRAME)
        mainFrame.minsize(Constants.FRAME_WIDTH, Constants.FRAME_HEIGHT)

        controller_main = MainController(mainFrame, Grid.grid_by_twenty())
        controller_main.run()
