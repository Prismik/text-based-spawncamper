from tile import Tile

class Door(Tile):
  def __init__(self):
    super().__init__()
    self.destroyable = False 
    self.isOpened = False
    self.armor = 100
    self.charRepresentation = 'd'
    self.canSeeThrough = False
    self.canBeMovedOnto = False
    self.lookedMessage = 'You see ' + 'an opened door' if self.isOpened else 'a closed door'

  def open(self):
    self.isOpened = true

  def close(self):
    self.isOpened = false

  def canLookThrough(self):
    return self.isOpened or (self.destroyable and self.armor <= 0)