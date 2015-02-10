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
		player.x = x
		player.y = y

	def playerMove(self, p):
		if dir == 0:
			if p.y - 1 >= 0:
				if self.at(p.x, p.y - 1) is None:
					self.movePlayerAt(p, p.x, p.y - 1)
					return True
		elif dir == 1:	
			if p.x + 1 < len(self.matrix[p.y]):
				if self.at(p.x + 1, p.y) is None:
					self.movePlayerAt(p, p.x + 1, p.y)
					return True
		elif dir == 2:
			if p.y + 1 < len(self.matrix):
				if self.at(p.x, p.y + 1) is None:
					self.movePlayerAt(p, p.x, p.y + 1)
					return True
		elif dir == 3:
			if p.x - 1 >= 0:
				if self.at(p.x - 1, p.y) is None:
					self.movePlayerAt(p, p.x - 1, p.y)
					return True

		return False

	def playerLook(self, p):
		return self.linearCollisionFrom(p.x, p.y, p.direction)

	def playerShoot(self, p):
		p.shoot()
		collision = self.linearCollisionFrom(p.x, p.y, p.direction)
		if collision is None:
			return None
		elif isinstance(collision, Player):
			collision.die()
			return collision

	def movePlayerAt(p, x, y):
		self.matrix[y][x] = None
		player.x = x
		player.y = y

	def linearCollisionFrom(self, x, y, dir):
		if dir == 0:
			for i in range(len(self.matrix) - y, 0, -1):
				if self.at(x, i) is not None:
					return self.at(x, i)
		elif dir == 1:
			for i in range(len(self.matrix[y]) - x):
				if self.at(i, y) is not None:
					return self.at(i, y)
		elif dir == 2:
			for i in range(len(self.matrix) - y):
				if self.at(x, i) is not None:
					return self.at(x, i)
		elif dir == 3:
			for i in range(len(self.matrix[y]) - x, 0, -1):
				if self.at(i, y) is not None:
					return self.at(i, y)

		return None
		
	def at(self, x, y):
		return self.matrix[y][x]