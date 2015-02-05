from direction import Direction
class Player:
	directions = ('North', 'East', 'South', 'West')

	def __init__(self, name):
		self.name = name
		self.direction = 0

	def die(self):
		print(name + " has died!")

	def turn(self, side):
		if side < 0:
			self.direction = (self.direction + 1) % 4
		else:
			self.direction = self.direction - 1 if self.direction > 0 else 3

		print("You are now looking " + str(self.direction))