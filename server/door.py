from tile import Tile

class Door(Tile):
  def __init__(self):
    self.destroyable = False 
    self.isOpened = False
    self.armor = 100
    super().__init__(False, False, 'd', 'You see ' + 'an opened door' if self.isOpened else 'a closed door')
  
  def open(self):
    self.isOpened = True
    self.canBeMovedOnto = True

  def close(self):
    self.isOpened = False
    self.canBeMovedOnto = False

  def canLookThrough(self):
    return self.isOpened or (self.destroyable and self.armor <= 0)