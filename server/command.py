class Command:
	def __init__(self, name, h, action):
		self.name = name
		self.help = h
		self.action = action

	def help(self):
		print(name + '\n' + h)

	def action(self):
		action()