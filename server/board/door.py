from . tile import Tile

class Door(Tile):
  def __init__(self, x, y):
    self.destroyable = False 
    self.opened = False
    self.armor = 100
    super().__init__(False, False, 'd', 'You see an opened door' if self.opened else 'You see a closed door', x, y)
  
  def open(self):
    self.opened = True
    self.passable = True
    return 'You opened a door'

  def close(self):
    self.opened = False
    self.passable = False
    return 'You closed a door'

  def canLookThrough(self):
    return self.opened or (self.destroyable and self.armor <= 0)
