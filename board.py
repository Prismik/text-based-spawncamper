from player import Player
class Board:
	def __init__(self, x, y):
		self.matrix = [[None for _ in range(y)] for _ in range(x)] 

	def printBoard(self):
		for y in range(len(self.matrix)):
			line = ''
			for x in range(len(self.matrix[y])):
				line += '_ '

			print(line)

	def addPlayer(self, player, x, y):
		self.matrix[y][x] = player

	def view(self):
		print('View')