class NotificationStack:
	def __init__(self, cnt):
		self.cnt = cnt
		self.stack = [''] * self.cnt
		self.len = 0
		self.index = 0

	def add(self, msg):
		self.len = self.len + 1 if self.len < self.cnt else self.cnt
		self.stack[self.index] = msg
		self.index = (self.index + 1) % self.cnt

	def printStack(self):
		for msg in self.stack:
			print(msg)