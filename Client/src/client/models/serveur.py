from time import sleep

from ivy.ivy import IvyServer

from core.models.grid import Grid
from core.models.position import Position


class MyAgent(IvyServer):

    def __init__(self, agent_name: str, is_client_to_send: bool) -> None:
        IvyServer.__init__(self, agent_name)
        self.start()
        self.is_client_to_send = is_client_to_send
        self.bind_msg(self.send_grid, "(grid)")
        self.bind_msg(self.send_grid_modification, "(position)")

    def send_grid(self, agent: 'MyAgent', grid: str):
        """
        fonction qui envoie la grille de départ à l'autre joueur
        :param grid: la grille initialiser sans modification
        :return: True si l'envoie c'est bien passer false sinon
        """
        if self.is_client_to_send:
            return Grid.rebulde(grid)
        else:
            return None

    def send_grid_modification(self, agent: 'MyAgent', position: str) -> Position:
        """
        :param position:
        :return:
        """
        return Position.rebuld(position)

    def __str__(self) -> str:
        return super().__str__()


if __name__ == '__main__':
    print('Ici on test le serveur')
    server = MyAgent("server", False)
    sleep(2)
    client = MyAgent("client", True)
    sleep(2)
    teste=Grid.grid_by_ten()

    server.send_msg(teste.__str__())
    pter=Position(1,2)
    client.send_msg(pter.__str__())
    sleep(3)
    print("faim")