from tkinter import Tk


class MainFrameView:
    """Classe qui représente un fenêtre"""

    def __init__(self, parent: Tk, controller) -> None:
        self.controller = controller
        self.parent = parent
        self.parent.columnconfigure(0, weight=1)
        self.parent.columnconfigure(1, weight=2)
