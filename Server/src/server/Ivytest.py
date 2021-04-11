from ivy.ivy import IvyServer
from time import sleep

class MyAgent(IvyServer):
    def __init__(self, agent_name, msg = 'hello world'):
        IvyServer.__init__(self, agent_name)
        self.start()
        self.bind_msg(self.on_hello, "hello world")

    def on_hello(self, agent) -> None:
        print("hello")

if __name__ == '__main__':
    a = MyAgent('007')  # server
    b = MyAgent('008')  # client

    sleep(3)
    b.send_msg('hello world')
