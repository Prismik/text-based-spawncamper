from player import Player

class Tile:
  def __init__ (self, canSeeThrough, canBeMovedOnto, charRepresentation, lookedMessage):
    self.messages = []
    self.entities = []
    self.canSeeThrough = canSeeThrough
    self.canBeMovedOnto = canBeMovedOnto
    self.charRepresentation = charRepresentation
    self.lookedMessage = lookedMessage

  def canLookThrough(self):
    if not self.canSeeThrough:
      return False

    for entity in self.entities:
      if not entity.canLookThrough():
        return False

    return True

  def canMoveTo(self):
    if not self.canBeMovedOnto:
      return False

    for entity in self.entities:
      if not entity.canMoveTo():
        return False

    return True

  def toChar(self):
    for entity in self.entities:
      if type(entity) is Player:
        return 'X'
    return self.charRepresentation

  def getLookedMessage(self):
    if self.canSeeThrough:
      return self.lookedMessage

    for entity in self.entities:
      if not entity.canLookThrough():
        return entity.getLookedMessage()

    return self.lookedMessage

  def hurt(self, source, damage):
    if self.entities:
      self.entities[0].hurt(source, damage)

  def addEntity(self, entity):
    self.entities.append(entity)

  def removeEntity(self, entity):
    self.entities.remove(entity)