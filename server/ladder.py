from tile import Tile

class Ladder(Tile):
  def __init__(self, goingUp):
    # Validate if this works
    super().__init__(False, True, 'L', 'You see a ladder ' + 'going up' if self.goingUp else 'going down')
 
    self.destroyable = False 

    self.goingUp = goingUp
