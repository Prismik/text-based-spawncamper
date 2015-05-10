import curses
import time
import threading

class NixInputHandler:
	def __init__(self, owner):
		self.terminated = False
		curses.wrapper(owner)
		print('Playing on a Unix sytem')

	def kbhit(self):
		ch = self.win.getch()
		if (ch != -1):
			curses.ungetch(ch)
			return 1
		else:
			return 0

	def setScreen(self, screen):
		self.win = screen
		self.win.nodelay(True) # non-blocking getch
		curses.cbreak() # no line buffering

	def pyin(self, prompt=None):
		if prompt:
			print(prompt)
		result = []
		while True:
			if self.kbhit() == 1:
				result.append(self.win.getch())
				if result[-1] in ['\r', '\n']:
					print
					return ''.join(result).rstrip()
			if self.terminated:
				return None
			time.sleep(0.1)	# just to yield to other processes/threads