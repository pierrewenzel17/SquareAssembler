from tkinter import Tk

from client.controllers import MainController


if __name__ == '__main__':
    root = Tk()
    root.title("Square Assembler")
    root.resizable(width=True, height=True)
    root.minsize(1200, 900)
    controller_main = MainController(root)
    controller_main.run()
