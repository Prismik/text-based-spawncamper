from entity import Entity

class Weapon(Entity):
  def __init__(self, name, cap):
    super().__init__()
    self.bullets = 0
    self.damage = 30
    self.capacity = cap

  def reload(self, ammount):
    self.bullets = min(self.capacity, ammount)
    return self.bullets

  def shoot(self):
    if self.bullets <= 0:
      return False
    else:
      self.bullets -= 1
      return True