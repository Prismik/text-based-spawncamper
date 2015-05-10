from . io.inputHandler import InputHandler

std = None
def io(owner=None):
	global std
	if (std == None):
		std = InputHandler(owner)

	return std