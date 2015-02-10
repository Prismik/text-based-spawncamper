from weapon import Weapon

class Player:
	directions = ('North', 'East', 'South', 'West')

	def __init__(self, name):
		self.x = 0
		self.y = 0
		self.bullets = 0
		self.weapon = Weapon('Pistol', 7)
		self.name = name
		self.direction = 0

	def die(self):
		print(name + ' has died!')

	def turn(self, side):
		if side < 0:
			self.direction = (self.direction + 1) % 4
		else:
			self.direction = self.direction - 1 if self.direction > 0 else 3

		print('You are now looking ' + str(self.direction))

	def shoot(self):
		return self.weapon.shoot()

	def reloadWeapon(self):
		if self.bullets <= 0:
			print('You need ammo.')
		else:
			usedBullets = self.weapon.reload(self.bullets)
			self.bullets -= usedBullets