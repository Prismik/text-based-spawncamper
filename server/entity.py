class Entity:
  def __init__(self):
    super().__init__()
    self.canSeeThrough = True
    self.canBeMovedOnto = True
    self.lookedMessage = 'You only see dust and rubbles'

  def hurt(self, source, damage):
    pass
    
  def canLookThrough(self):
    return self.canSeeThrough

  def canMoveTo(self):
    return self.canBeMovedOnto

  def getLookedMessage(self):
    return self.lookedMessage