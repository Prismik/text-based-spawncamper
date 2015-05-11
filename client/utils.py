from . io.inputHandler import InputHandler

std = None
def io(screen=None):
	global std

	print(screen)
	if (std is None):
		std = InputHandler(screen)

	print(std)
	return std