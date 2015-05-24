import platform
import client.utils as utils
from . io.colorama import Fore, Back, Style
class GameUI:
  def __init__(self, name):
    self.name = name
    self.playerBullets = 0
    self.gunBullets = 0
    self.gunCapacity = 0
    self.direction = 0
    self.hp = 0

  def update(self, data):
    self.playerBullets = data['bullets']
    self.gunBullets = data['gun']['bullets']
    self.gunCapacity = data['gun']['cap']
    self.direction = data['dir']
    self.hp = data['hp']

  def printUI(self):
    self.printStatus()
    self.printCompass()

  def greenPrint(self, msg):
    utils.std.pyout(Fore.GREEN + msg)

  def printCompass(self):
    if self.direction == 0:
      self.greenPrint("      N      ")
      self.greenPrint("   __---__   ")
      self.greenPrint("  -   ^   -  ")
      self.greenPrint("W|    |    |E")
      self.greenPrint("  _       _  ")
      self.greenPrint("   --___--   ")
      self.greenPrint("      S      ")
    elif self.direction == 1:
      self.greenPrint("      N      ")
      self.greenPrint("   __---__   ")
      self.greenPrint("  -       -  ")
      self.greenPrint("W|    ---> |E")
      self.greenPrint("  _       _  ")
      self.greenPrint("   --___--   ")
      self.greenPrint("      S      ")
    elif self.direction == 2:
      self.greenPrint("      N      ")
      self.greenPrint("   __---__   ")
      self.greenPrint("  -       -  ")
      self.greenPrint("W|    |    |E")
      self.greenPrint("  _   v   _  ")
      self.greenPrint("   --___--   ")
      self.greenPrint("      S      ")
    elif self.direction == 3:
      self.greenPrint("      N      ")
      self.greenPrint("   __---__   ")
      self.greenPrint("  -       -  ")
      self.greenPrint("W| <---    |E")
      self.greenPrint("  _       _  ")
      self.greenPrint("   --___--   ")
      self.greenPrint("      S      ")

  def printStatus(self):
    heart = "O" if platform.system() == 'Windows' else "\u2764"

    gun = "Ammo ["
    b = self.gunBullets
    for i in range(self.gunCapacity):
      if b != 0:
        gun += "|"
        b -= 1
      else:
        gun += " "

    gun += "]"
    utils.std.pyout(Back.GREEN + ' ' + Fore.BLACK + self.name + ' ' +
      Fore.RED + heart + 
      Fore.BLACK + '  ' + str(self.hp) + ' | ' + gun)