import asyncore, socket, os, threading, json
from command import Command
from board import Board
from player import Player
from notificationStack import NotificationStack
from gameUI import GameUI

class Client(asyncore.dispatcher):
	def __init__(self, host, port, name):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((host, port))
		self.stack = NotificationStack(1)
		self.ui = GameUI()
		self.name = name

	def handle_connect(self):
		self.stack.add('You are now connected.')

	def handle_close(self):
		self.stack.add('Client: Connection Closed')
		self.close()

	def handle_read(self):
		data = self.recv(1024)

		if not data:
			return

		data = json.loads(data.decode().strip())
		if data['what'] == 'result':
			if data['value'] == 'dead':
				threading.Thread(target=asyncore.loop, name="Asyncore Loop").exit()
			else:
				self.stack.add(data['value'])
				self.ui.update(data['state'])
		else:
			self.stack.add(data['what'])

	def start(self):
		commands = ['look', 'turn left', 'turn right', 'shoot', 'move', 'reload']
		threading.Thread(target=asyncore.loop, name="Asyncore Loop").start()

		while True:
			os.system('clear')
			self.ui.printUI()
			self.stack.printStack()
			action = input('What to do: ')
			if action in commands:
				data = json.dumps({'what':action, 'who':self.name})
				self.send(data.encode())


