from tile import Tile
from config import propertyValue

class Wall(Tile):
  def __init__(self):
    super().__init__()
    # Allows the wall to be destroyed by bullets stronger than it's armor
    self.destroyable = propertyValue("Wall.destroyable") == "True"
    # Allows Look to go through this wall but without great info
    self.canSeeThrough = False
    self.canBeMovedOnto = False
    # The bullets damage soaked by the wall. The rest goes through
    self.armor = 100

    self.charRepresentation = 'i'

    self.lookedMessage = 'You see a marvelously crafted wall'

  def canLookThrough(self):
    return self.canSeeThrough

  def canMoveTo(self):
    return self.canBeMovedOnto

  def hurt(self, source, damage):
    if self.destroyable:
        self.armor -= damage
        if self.armor <= 0:
            self.destroy()

  def destroy(self):
    self.canSeeThrough = True
    self.canBeMovedOnto = True
    self.charRepresentation = 'O'