

from ivy.std_api import *
IvyInit("my agent")
IvyStart()
import time

from ivy.ivy import IvyServer

class MyAgent(IvyServer):
  def __init__(self, agent_name):
    IvyServer.__init__(self,agent_name)
    self.start('127.255.255.255:2010')
    self.bind_msg(self.handle_hello, 'hello .*')
    self.bind_msg(self.handle_button, 'BTN ([a-fA-F0-9]+)')

  def handle_hello(self, agent):
    print('[Agent %s] GOT hello from %r'%(self.agent_name, agent))

  def handle_button(self, agent, btn_id):
    print('[Agent %s] GOT BTN button_id=%s from %r'%(self.agent_name, btn_id, agent))
    # let's answer!
    self.send_msg('BTN_ACK %s'%btn_id)

a=MyAgent('007')
