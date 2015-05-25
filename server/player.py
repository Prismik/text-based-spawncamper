from entity import Entity
from weapon import Weapon

class Player(Entity):
  directions = ('North', 'East', 'South', 'West')

  def __init__(self, name):
    super().__init__()
    self.handler = None
    self.x = 0
    self.y = 0
    self.bullets = 999 # Should be enough in a single game
    self.hp = 100
    self.weapon = Weapon('Pistol', 7)
    self.name = name
    self.direction = 0
    self.lookedMessage = 'You see ' + self.name + ' moving in the shadow'

  def hurt(self, by, points):
    self.hp -= points
    if (self.hp <= 0):
      self.die(by)

  def die(self, by):
    self.handler.sendJson({'what':'dead', 'who': by})

  def turn(self, side):
    if side > 0:
      self.direction = (self.direction + 1) % 4
    else:
      self.direction = self.direction - 1 if self.direction > 0 else 3

    return 'You are now looking ' + Player.directions[self.direction]

  def shoot(self):
    return self.weapon.shoot()

  def reloadWeapon(self):
    if self.bullets <= 0:
      return 'You cleverly load air into your gun'
    else:
      usedBullets = self.weapon.reload(self.bullets)
      if usedBullets == 0:
        self.bullets -= 1
        return 'Your try to load a bullet, but it falls to the floor'
      else:
        self.bullets -= usedBullets
        return 'You put ' + str(usedBullets) + ' bullets in your gun'