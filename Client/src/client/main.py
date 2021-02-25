from tkinter import Tk

from client.controllers.main_controller import MainController
from client.utils.constant_util import Constants


if __name__ == '__main__':
    root = Tk()
    root.title(Constants.GAME_TITLE)
    root.resizable(width=Constants.RESIZE_FRAME, height=Constants.RESIZE_FRAME)
    root.minsize(Constants.FRAME_WIDTH, Constants.FRAME_HEIGHT)
    controller_main = MainController(root)
    controller_main.run()
