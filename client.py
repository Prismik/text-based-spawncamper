import asyncore, socket, os, threading
from command import Command
from board import Board
from player import Player
from notificationStack import NotificationStack

class Client(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host, port))
		self.me = Player('A player')
		self.board = Board(7, 7)
		self.board.addPlayer(self.me, 0, 0)
		self.stack = NotificationStack()

	def handle_connect(self):
		self.stack.add('Client: Connection Incoming')

	def handle_close(self):
		self.stack.add('Client: Connection Closed')
		self.close()

	#def handle_write(self):
	#	sent = self.send(self.write_buffer)
	#	self.logger.debug('handle_write() -> "%s"', self.write_buffer[:sent])
	#	self.write_buffer = self.write_buffer[sent:]

	def handle_read(self):
		data = self.recv(1024)
		if not data:
			return
			
		self.stack.add(data.decode('utf-8'))
		self.send(b'Hello Client')

c = Client('127.0.0.1', 5037)
commands = { 
	'view': Command('view', 'Look out for ennemies in front of you.', c.board.view), 
	'turn left': Command('turn left', 'Turn to your left.', lambda: c.me.turn(-1)),
	'turn right': Command('turn right', 'Turn to your right.', lambda: c.me.turn(1))
}
threading.Thread(target=asyncore.loop, name="Asyncore Loop").start()

while True:
	os.system('clear')
	c.stack.printStack()
	action = input('What to do: ')
	if action in commands:
		commands.get(action).action()
		c.send(action.encode())
