import msvcrt
import time

class WinInputHandler:
	def __init__(self):
		self.terminated = False
		print('Playing on a Windows system')

	def pyin(self, prompt=None):
		if prompt:
			print(prompt)
		result = []
		while True:
			if msvcrt.kbhit():
				result.append(msvcrt.getche())
				if result[-1] in ['\r', '\n']:
					print
					return ''.join(result).rstrip()
			if self.terminated:
				return None
			time.sleep(0.1)	# just to yield to other processes/threads