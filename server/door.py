from tile import Tile

class Door(Tile):
  def __init__(self):
    # Validate if this works
    super().__init__(self, False, False, 'd', 'You see ' + 'an opened door' if self.isOpened else 'a closed door')
    self.destroyable = False 
    self.isOpened = False
    self.armor = 100

  def open(self):
    self.isOpened = true

  def close(self):
    self.isOpened = false

  def canLookThrough(self):
    return self.isOpened or (self.destroyable and self.armor <= 0)