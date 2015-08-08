from player import Player

class Tile:
  def __init__ (self, canSeeThrough, passable, charRepresentation, description):
    self.messages = []
    self.entities = []
    self.canSeeThrough = canSeeThrough
    self.passable = passable
    self.charRepresentation = charRepresentation
    self.description = description

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

