from client.views import ScoreView


class ScoreController:

    def __init__(self, parent) -> None:
        self.parent = parent
        self.view = ScoreView(parent, self)
