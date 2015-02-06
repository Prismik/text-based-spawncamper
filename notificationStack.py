class NotificationStack:
	def __init__(self):
		self.stack = [''] * 7
		self.len = 0
		self.index = 0

	def add(self, msg):
		self.len = self.len + 1 if self.len < 7 else 7
		self.stack[self.index] = msg
		self.index = (self.index + 1) % 7

	def printStack(self):
		for msg in self.stack:
			print(msg)