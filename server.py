import asyncore, socket, json
from command import Command
from board import Board
from player import Player



class Handler(asyncore.dispatcher):
	def __init__(self, sock, player, board):
		asyncore.dispatcher.__init__(self, sock)
		self.player = player
		self.board = board
		self.commands = {
			'look': Command('look', 'Look out for ennemies in front of you.', lambda: board.playerLook(self.player)), 
			'turn left': Command('turn left', 'Turn to your left.', lambda: player.turn(-1)),
			'turn right': Command('turn right', 'Turn to your right.', lambda: player.turn(1)),
			'shoot': Command('shoot', 'Shoot in front of you.', lambda: board.playerShoot(self.player)),
			'move': Command('move', 'Move where you are looking.', lambda: board.playerMove(self.player)),
			'reload': Command('reload', 'Put some clips in your weapon.', lambda: player.reloadWeapon())
		}

	def handle_read(self):
		data = self.recv(1024)
		if not data:
			return

		data = json.loads(data.decode().strip())
		if data['what'] in self.commands:
			result = self.commands.get(data['what']).action()
			self.send(json.dumps({'what':'result', 'value':result, 'who':'server'}).encode())

	def handle_close(self):
		print('Connection Closed')
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
		sock.send(json.dumps({'what':'handshake', 'who':'server'}).encode())
		self.HANDLER(sock, player, self.board)

	def serve(Self):
		asyncore.loop()

s = Server('0.0.0.0', 5017)
s.serve()