from tkinter import Tk

from client.controllers.welcome_controller import WelcomeController
from client.utils.constant_util import Constants

if __name__ == '__main__':
    root = Tk()
    root.title(Constants.GAME_TITLE)
    root.geometry("595x475+400+150")
    root.resizable(width=False, height=False)
    welcome_controller = WelcomeController(root)
    welcome_controller.run()
