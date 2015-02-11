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
		if p.direction == 0:
			if p.y != 0:
				if self.at(p.x, p.y - 1) is None:
					self.movePlayerAt(p, p.x, p.y - 1)
					return 'You successfully moved north'
		elif p.direction == 1:	
			if p.x != len(self.matrix[p.y]) - 1:
				if self.at(p.x + 1, p.y) is None:
					self.movePlayerAt(p, p.x + 1, p.y)
					return 'You successfully moved east'
		elif p.direction == 2:
			if p.y != len(self.matrix) - 1:
				if self.at(p.x, p.y + 1) is None:
					self.movePlayerAt(p, p.x, p.y + 1)
					return 'You successfully moved south'
		elif p.direction == 3:
			if p.x != 0:
				if self.at(p.x - 1, p.y) is None:
					self.movePlayerAt(p, p.x - 1, p.y)
					return 'You successfully moved west'

		return 'You could not move'

	def playerLook(self, p):
		vision = self.linearCollisionFrom(p.x, p.y, p.direction)
		if vision is None:
			return 'You only see dust and rubbles'
		else:
			return 'You see something moving in the shadow'

	def playerShoot(self, p):
		if p.shoot():
			collision = self.linearCollisionFrom(p.x, p.y, p.direction)
			if collision is None:
				return 'You successfully hit nothing'
			elif isinstance(collision, Player):
				collision.die()
				return 'You killed a player'
		else:
			return 'Your weapon is empty'

	def movePlayerAt(self, p, x, y):
		self.matrix[p.y][p.x] = None
		self.matrix[y][x] = p
		p.x = x
		p.y = y

	def linearCollisionFrom(self, x, y, dir):
		if dir == 0 and y != 0:
			for i in range(y - 1, 0, -1):
				if self.at(x, i) is not None:
					return self.at(x, i)
		elif dir == 1 and x != len(self.matrix[y]) - 1:
			for i in range(x + 1, len(self.matrix[y]) - 1):
				if self.at(i, y) is not None:
					return self.at(i, y)
		elif dir == 2 and y != len(self.matrix) - 1:
			for i in range(y + 1, len(self.matrix) - 1):
				if self.at(x, i) is not None:
					return self.at(x, i)
		elif dir == 3 and x != 0:
			for i in range(x - 1, 0, -1):
				if self.at(i, y) is not None:
					return self.at(i, y)

		return None
		
	def at(self, x, y):
		return self.matrix[y][x]