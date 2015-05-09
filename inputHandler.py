import platform
try:
	from winInput import WinInputHandler
except ImportError:
	from nixInput import NixInputHandler	

class InputHandler:
	def __init__(self, owner):
		self.handler = None
		sys = platform.system()
		if (sys == 'Windows'):
			self.handler = WinInputHandler()
		elif (sys == 'Linux' or sys == 'Darwin'):
			self.handler = NixInputHandler(owner)
		else:
			print ('OS not supported') # TODO Handle that

	def pyin(self, prompt=None):
		return self.handler.pyin(prompt)

	def setScreen(self, screen):
		self.handler.setScreen(screen)

	def terminate(self):
		self.handler.terminated = True