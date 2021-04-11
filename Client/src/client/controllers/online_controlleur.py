
class OnlineControlleur:
    def __init__(self):
        pass

    def create_game(self, view):
        print("I create a new game")
        view.mainloop()

    def join_game(self, view):
        print("I join a new game")
        view.mainloop()

    def rollback(self, view):
        print("I rollback")
        view.destroy()
