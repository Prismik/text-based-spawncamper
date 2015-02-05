from board import Board
class Board:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.player = None

	def printBoard(self):
		for i in range(self.y):
			line = ""
			for j in range(self.x):
				line += "_"

			print(line)

	def addPlayer(self, x, y):
		self.player = Player(x, y)

	def view
