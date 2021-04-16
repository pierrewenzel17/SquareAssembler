from enum import Enum
from time import sleep

from ivy.ivy import IvyServer

from core.models.grid import Grid
from core.models.position import Position


class StateOnline(Enum):
    CREATE = True
    JOIN = False

    def __eq__(self, o) -> bool:
        if isinstance(o, StateOnline):
            return self.name == o.name
        return False


class MyAgent(IvyServer):

    def __init__(self, agent_name: str, state) -> None:
        IvyServer.__init__(self, agent_name, f'connect={state.name}')

    def __str__(self) -> str:
        return super().__str__()


if __name__ == '__main__':
    print('Ici on test le serveur')
    server = MyAgent("server")
    sleep(2)
    server2 = MyAgent("client")
    sleep(2)
    server.send_msg(f'connect=({StateOnline.CREATE.name})')
    '''
    teste = Grid.grid_by_ten()
    server.send_msg(teste.__str__())
    pter = Position(1, 2)
    client.send_msg(pter.__str__())
    sleep(3)'''
    print("faim")
