class Weapon:
	def __init__(self, name, cap):
		self.bullets = 0
		self.capacity = cap

	def reload(self, ammount):
		self.bullets = min(self.capacity, ammount)
		return self.bullets

	def shoot(self):
		if self.bullets <= 0:
			return False
		else:
			self.bullets -= 1
			return True