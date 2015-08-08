from tile import Tile

class Ladder(Tile):
  def __init__(self, goingUp):
    super().__init__(False, True, 'L', 'You see a ladder going up' if self.goingUp else 'You see a ladder going down')
    self.destroyable = False 
    self.goingUp = goingUp
