from weapon import Weapon

class Player:
	directions = ('North', 'East', 'South', 'West')

	def __init__(self, name):
		self.handler = None
		self.x = 0
		self.y = 0
		self.bullets = 999 # Should be enough in a single game
		self.weapon = Weapon('Pistol', 7)
		self.name = name
		self.direction = 0

	def die(self, by):
		self.handler.send(json.dumps({'what':'dead', 'who': by}).encode())

	def turn(self, side):
		if side > 0:
			self.direction = (self.direction + 1) % 4
		else:
			self.direction = self.direction - 1 if self.direction > 0 else 3

		return 'You are now looking ' + Player.directions[self.direction]

	def shoot(self):
		return self.weapon.shoot()

	def reloadWeapon(self):
		if self.bullets <= 0:
			return 'You cleverly load air into your gun'
		else:
			usedBullets = self.weapon.reload(self.bullets)
			if usedBullets == 0:
				self.bullets -= 1
				return 'Your try to load a bullet, but it falls to the floor'
			else:
				self.bullets -= usedBullets
				return 'You put ' + str(usedBullets) + ' bullets in your gun'