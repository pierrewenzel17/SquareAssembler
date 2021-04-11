from client.views.welcome_view import WelcomeView


class WelcomeController:
    def __init__(self, root):
        self.parent = root
        self.view = WelcomeView(self, self.parent)

    def run(self):
        self.parent.wm_attributes("-transparentcolor", "grey")
        self.parent.mainloop()
