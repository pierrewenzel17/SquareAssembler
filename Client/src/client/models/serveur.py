from ivy.ivy import IvyServer

from core.models.grid import Grid


class Server(IvyServer):
    def __init__(self, server_name: str) -> None:
        super().__init__(self, server_name)
        self.start("127.0.0.1:8080")

    def send_grid(self, grid: Grid) -> bool:
        """
        fonction qui envoie la grille de départ à l'autre joueur
        :param grid: la grille initialiser sans modification
        :return: True si l'envoie c'est bien passer false sinon
        """
        return True

    def send_grid_modification(self):
        pass


if __name__ == '__main__':
    print('Ici on test le serveur')
