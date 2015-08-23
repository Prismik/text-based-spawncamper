from . tile import Tile

class Wall(Tile):
  def __init__(self, x, y):
    super().__init__(False, False, 'i', 'You see a marvelously crafted wall', x, y)
    # Allows the wall to be destroyed by bullets stronger than it's armor
    self.destroyable = False

    # The bullets damage soaked by the wall. The rest goes through
    self.armor = 100

  def hurt(self, source, damage):
    if self.destroyable:
        self.armor -= damage
        if self.armor <= 0:
            self.destroy()

  def destroy(self):
    self.canSeeThrough = True
    self.passable = True
    self.charRepresentation = 'O'
