from time import sleep

from server.Ivytest import MyAgent


class OnlineControlleur:
    def __init__(self):
        pass

    def create_game(self, view):

        view.mainloop()
        server = MyAgent("server", False)
        sleep(2)
        """
        Création d'un statue (client serveur)
        si notre statut = serveur
            send grille
        
        
        """



    def join_game(self, view):
        print("I join a new game")
        view.mainloop()

    def rollback(self, view):
        print("I rollback")
        view.destroy()
