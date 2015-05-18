import threading
import os
from . colorama import Fore, Back, Style

class BasicInputHandler:
  def __init__(self, system):
    self.system = system

  def pyin(self, prompt=None):
    return input(prompt)

  def pyout(self, msg):
    print(msg + Fore.RESET + Back.RESET + Style.RESET_ALL)
    # print(Fore.RESET + Back.RESET + Style.RESET_ALL)

  def clear(self):
    # print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    if (self.system == 'Windows'):
      os.system('cls')
    else:
      os.system('clear')
