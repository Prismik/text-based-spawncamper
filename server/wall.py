from tile import Tile

class Wall(Tile):
  def __init__(self):
    super().__init__()
    # Allows the wall to be destroyed by bullets stronger than it's armor
    self.destroyable = False 
    # Allows Look to go through this wall but without great info
    self.canSeeThrough = False
    self.canBeMovedOnto = False
    # The bullets damage soaked by the wall. The rest goes through
    self.armor = 100

    self.charRepresentation = 'i'

    self.lookedMessage = 'You see a marvelously crafted wall'

  def canLookThrough(self):
    return self.destroyable and self.armor <= 0

  def canMoveTo(self):
    return self.destroyable and self.armor <= 0
