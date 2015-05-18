from . io.inputHandler import InputHandler

std = None
def io(screen=None):
  global std

  if (std is None):
    std = InputHandler(screen)