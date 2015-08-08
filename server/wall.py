from tile import Tile

class Wall(Tile):
  def __init__(self):
    super().__init__(False, False, 'i', 'You see a marvelously crafted wall')
    # Allows the wall to be destroyed by bullets stronger than it's armor
    self.destroyable = True

    # The bullets damage soaked by the wall. The rest goes through
    self.armor = 100

  
  # TODO Do we need a setter ?
  # Why doesn't it use the super class function ?
  @property
  def canLookThrough(self):
    return self.canSeeThrough

  # TODO Do we need a setter ?
  # Why doesn't it use the super class function ?
  @property
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