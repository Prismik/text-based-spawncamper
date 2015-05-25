from player import Player

class Tile:
  def __init__ (self):
    self.messages = []
    self.entities = []
    self.canSeeThrough = True
    self.canBeMovedOnto = True
    self.charRepresentation = 'O'
    self.lookedMessage = 'You only see dust and rubbles'

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

  def addEntity(self, entity):
    self.entities.append(entity)

  def removeEntity(self, entity):
    self.entities.remove(entity)