import os
from tkinter import PhotoImage, Canvas, Button, CENTER, NW, Label, Tk

from client.controllers.main_controller import MainController
from client.utils.constant_util import Constants


class WelcomeView:
    def __init__(self, controller, root):
        self.controller = controller
        self.root = root
        self.bg = PhotoImage(file=os.path.join(os.getcwd(), 'resources/bg_image.gif'))
        self.canvas = Canvas(self.root, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.btnPlay = Button(self.canvas, text="Play", font=("Courier", 45, "bold"), command=self.runGame) \
            .place(relx=0.5, rely=0.3, anchor=CENTER)
        self.btnQuit = Button(self.canvas, text="Quit", font=("Courier", 45, "bold"), command=self.root.quit) \
            .place(relx=0.5, rely=0.5, anchor=CENTER)
        self.createdBy = Label(self.canvas, text="Created by BURTIN Cyril, WENZEL Pierre & PHILIPP Sebastien ",
                               font=("Courier", 10), bg="lightgrey") \
            .place(relx=0.5, rely=0.7, anchor=CENTER)

        self.canvas.create_window(10, 10, anchor=NW, window=self.btnPlay)
        self.canvas.create_window(10, 10, anchor=NW, window=self.btnQuit)
        self.canvas.create_window(10, 10, anchor=NW, window=self.createdBy)

    def runGame(self):
        self.root.destroy()
        mainFrame = Tk()
        mainFrame.title(Constants.GAME_TITLE)
        mainFrame.resizable(width=Constants.RESIZE_FRAME, height=Constants.RESIZE_FRAME)
        mainFrame.minsize(Constants.FRAME_WIDTH, Constants.FRAME_HEIGHT)
        controller_main = MainController(mainFrame)
        controller_main.run()
