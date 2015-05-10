class GameUI:
	def __init__(self):
		self.playerBullets = 0
		self.gunBullets = 0
		self.gunCapacity = 0
		self.direction = 0

	def update(self, data):
		self.playerBullets = data['bullets']
		self.gunBullets = data['gun']['bullets']
		self.gunCapacity = data['gun']['cap']
		self.direction = data['dir']

	def printUI(self):
		self.printCompass()
		self.printGun()

	def printCompass(self):
		if self.direction == 0:
			print("      N      ")
			print("   __---__   ")
			print("  -   ^   -  ")
			print("W|    |    |E")
			print("  _       _  ")
			print("   --___--   ")
			print("      S      ")
		elif self.direction == 1:
			print("      N      ")
			print("   __---__   ")
			print("  -       -  ")
			print("W|    ---> |E")
			print("  _       _  ")
			print("   --___--   ")
			print("      S      ")
		elif self.direction == 2:
			print("      N      ")
			print("   __---__   ")
			print("  -       -  ")
			print("W|    |    |E")
			print("  _   v   _  ")
			print("   --___--   ")
			print("      S      ")
		elif self.direction == 3:
			print("      N      ")
			print("   __---__   ")
			print("  -       -  ")
			print("W| <---    |E")
			print("  _       _  ")
			print("   --___--   ")
			print("      S      ")

	def printGun(self):
		gun = "Ammo ["
		b = self.gunBullets
		for i in range(self.gunCapacity):
			if b != 0:
				gun += "|"
				b -= 1
			else:
				gun += " "

		gun += "]"
		print(gun)