from tkinter import Tk

from client.controllers.main_controller import MainController
from client.utils.constant_util import Constants
from client.views.welcome_view import WelcomeView


class WelcomeController:
    def __init__(self, root):
        self.parent = root
        self.view = WelcomeView(self, self.parent)

    def run(self):
        self.parent.mainloop()
