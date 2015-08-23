import asyncore, socket, os, threading, json
import client.utils as utils
from . notificationStack import NotificationStack
from . gameUI import GameUI 

class Client(asyncore.dispatcher):
  def __init__(self, host, port, name):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connect((host, port))
    self.stack = NotificationStack(3)
    self.ui = GameUI(name)
    self.name = name
    self.terminated = False

  def handle_connect(self):
    self.stack.add('You are now connected.')

  def handle_close(self):
    self.stack.add('You have left the game: Press enter to continue')
    self.close()

  def handle_read(self):
    data = self.recv(1024)

    if not data:
      self.terminate()
      return

    data = json.loads(data.decode().strip())
    if data['what'] == 'result':
      if data['value'] == 'dead':
        self.stack.add('You have been killed. Press enter to leave')
        self.terminate()
      else:
        self.stack.add(data['value'])
        self.ui.update(data['state'])
    elif data['what'] == 'hear':
      self.stack.add(data['sound'])
    else:
      self.stack.add(data['what'])

  def terminate(self):
    self.terminated = True

  def start(self):
    commands = ['open', 'close', 'look', 'turn left', 'turn right', 'shoot', 'move', 'reload', 'exit']
    threading.Thread(target=asyncore.loop, name="Asyncore Loop").start()

    while not self.terminated:
      utils.std.clear()
      self.ui.printUI()
      self.stack.printStack()
      action = utils.std.pyin('> ')
      if not self.terminated:
        if action in commands:
          data = json.dumps({'what': action, 'who': self.name})
          self.send(data.encode())
      else:
        utils.std.clear()

