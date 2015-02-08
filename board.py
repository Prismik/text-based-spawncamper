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

	def findPlayer(self, obj):
		for y in range(len(self.matrix)):
			for x in range(len(self.matrix[y])):
				if self.at(x, y) == obj:
					return self.at(x, y)

	def movePlayer(self):
		print('Moved')

	def killPlayer(self, player):
		findPlayer(player).die()

	def playerShoot(self, player):
		player.shoot()

	def linearCollisionFrom(self, x, y, dir):
		if dir == 0:
			for i in range(len(self.matrix) - y, 0, -1):
				if self.at(x, i) is None:
					return self.at(x, i)
		elif dir == 1:
			for i in range(len(self.matrix[y]) - x):
				if self.at(i, y) is None:
					return self.at(i, y)
		elif dir == 2:
			for i in range(len(self.matrix) - y):
				if self.at(x, i) is None:
					return self.at(x, i)
		elif dir == 3:
			for i in range(len(self.matrix[y]) - x, 0, -1):
				if self.at(i, y) is None:
					return self.at(i, y)
		
	def at(self, x, y):
		return self.matrix[y][x]

	def view(self):
		print('View')