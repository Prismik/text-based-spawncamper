import platform
try:
	from . winInput import WinInputHandler
except ImportError:
	from . nixInput import NixInputHandler	

class InputHandler:
	def __init__(self, window=None):
		self.handler = None
		sys = platform.system()
		if (sys == 'Windows'):
			self.handler = WinInputHandler()
		elif (sys == 'Linux' or sys == 'Darwin'):
			self.handler = NixInputHandler(window)
		else:
			pass # TODO Handle that

	def pyin(self, prompt=None):
		return self.handler.pyin(prompt)

	def pyout(self, msg):
		self.handler.pyout(msg)

	def terminate(self):
		self.handler.terminated = True