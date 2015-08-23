from entity.player import Player

class Tile:
  def __init__(self, canSeeThrough, passable, charRepresentation, description, x, y):
    self.messages = []
    self.entities = []
    self.linkedTiles = set()
    self.canSeeThrough = canSeeThrough
    self.passable = passable
    self.charRepresentation = charRepresentation
    self.description = description
    self.x = x
    self.y = y

  def __hash__(self):
    return hash(self.x + self.y * 10)
  
  def __eq__(self, other):
    if type(other) is Tile:
      return ((self.x == other.x) and (self.y == other.y))
    else:
      return False
  
  def __ne__(self, other):
    return (not self.__eq__(other))

  def describe(self):
    for entity in self.entities:
      if type(entity) is Player:
        return entity.description

    return self.description

  def canLookThrough(self):
    if not self.canSeeThrough:
      return False

    for entity in self.entities:
      if not entity.canSeeThrough:
        return False

    return True

  def canMoveTo(self):
    if not self.passable:
      return False

    for entity in self.entities:
      if not entity.passable:
        return False

    return True

  def toChar(self):
    for entity in self.entities:
      if type(entity) is Player:
        return 'X'

    return self.charRepresentation

  def hurt(self, source, damage):
    for entity in self.entities:
      entity.hurt(source, damage)

  def addEntity(self, entity):
    self.entities.append(entity)

  def removeEntity(self, entity):
    self.entities.remove(entity)
  
  def emit(self, sound, amplitude):
    if amplitude >= 0:
      for tile in self.linkedTiles:
        tile.propagate(sound, amplitude - 1, set([self]))

  def propagate(self, sound, amplitude, propagatedTiles):
    propagatedTiles.add(self)
    tilesToPropagate = self.linkedTiles.difference(propagatedTiles)
    for tile in tilesToPropagate:
      tile.propagate(sound, amplitude - 1, propagatedTiles)

    for entity in self.entities:
      if type(entity) is Player:
        entity.hear(sound)
