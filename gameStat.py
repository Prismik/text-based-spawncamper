class GameStat:
	def __init__(self):
		self.rotations = 0
		self.move = 0
		self.hit = 0
		self.missed = 0
		self.kill = 0

	def printStats(self):
		print('You did ' + self.ritations + ' rotations.')