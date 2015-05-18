import asyncore, socket, json
from command import Command
from board import Board
from player import Player

class Handler(asyncore.dispatcher):
  def __init__(self, sock, player, board):
    asyncore.dispatcher.__init__(self, sock)
    self.player = player
    self.player.handler = self
    self.board = board
    self.commands = {
      'look': Command('look', 'Look out for ennemies in front of you.', lambda: board.playerLook(self.player)), 
      'turn left': Command('turn left', 'Turn to your left.', lambda: player.turn(-1)),
      'turn right': Command('turn right', 'Turn to your right.', lambda: player.turn(1)),
      'shoot': Command('shoot', 'Shoot in front of you.', lambda: board.playerShoot(self.player)),
      'move': Command('move', 'Move where you are looking.', lambda: board.playerMove(self.player)),
      'reload': Command('reload', 'Put some clips in your weapon.', lambda: player.reloadWeapon()),
      'exit': Command('exit', 'Leave the game.', lambda: self.playerExit())
    }
    self.sendResult()

  def playerExit(self):
    self.board.removePlayer(self.player) 
    self.handle_close()

  def handle_read(self):
    data = self.recv(1024)
    if not data:
      return

    data = json.loads(data.decode().strip())
    if data['what'] in self.commands:
      result = self.commands.get(data['what']).action()
      self.sendResult()

      self.board.printBoard()

  def sendJson(self, json):
    self.send(json.dumps(json).encode())

  def sendResult(self):
    self.sendJson({'what':'result', 
                            'value':result, 
                            'state': {
                              'hp': self.player.hp,
                              'bullets': self.player.bullets, 
                              'gun': {
                                'bullets': self.player.weapon.bullets,
                                'cap': self.player.weapon.capacity
                              },
                              'dir': self.player.direction
                            }, 
                            'who':'server'})

  def handle_close(self):
    print('Connection Closed')
    self.sendJson({'what': 'close'})
    self.close()

class Server(asyncore.dispatcher):
  def __init__(self, host, port):
    self.HANDLER = Handler
    self.board = Board(7, 7)
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.bind((host, port))
    self.listen(5)
    print('Waiting for connection...')
    self.connections = []

  def handle_accept(self):
    (sock, addr) = self.accept()
    self.connections.append(socket)
    print('Connection by ', addr)
    player = Player(str(addr))
    self.board.addPlayer(player, 0, 0)
    self.HANDLER(sock, player, self.board)

  def serve(self):
    asyncore.loop()

s = Server('0.0.0.0', 5017)
s.serve()