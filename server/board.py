from player import Player
from wall import Wall
from door import Door

class Board:
  def __init__(self, x, y):
    self.matrix = [[None for _ in range(y)] for _ in range(x)] 
    with open('map' + str(y) + str(x), 'r') as mapFile:
      for i, line in enumerate(mapFile):
        for j, tile in enumerate(line):
          if tile != '\n':
            self.matrix[i][j] = self.parseTile(tile)

    self.printBoard()

  def parseTile(self, char):
    return {
      '0': None,
      'i': Wall(),
      'd': Door()
    }[char]

  def printBoard(self):
    for y in range(len(self.matrix)):
      line = ''
      for x in range(len(self.matrix[y])):
        tile = self.matrix[y][x]
        if tile == None:
          line += 'O '
        elif type(tile) is Player:
          line += 'X '
        elif type(tile) is Door:
          line += 'd '
        elif type(tile) is Wall:
          line += 'i '
      print(line)

  def addPlayer(self, player, x, y):
    self.matrix[y][x] = player
    player.x = x
    player.y = y

  def removePlayer(self, player):
    self.matrix[player.y][player.x] = None
    
  # TODO handle doors and walls
  def playerMove(self, p):
    if p.direction == 0:
      if p.y != 0:
        if self.at(p.x, p.y - 1) is None:
          self.movePlayerAt(p, p.x, p.y - 1)
          return 'You successfully moved north'
    elif p.direction == 1:  
      if p.x != len(self.matrix[p.y]) - 1:
        if self.at(p.x + 1, p.y) is None:
          self.movePlayerAt(p, p.x + 1, p.y)
          return 'You successfully moved east'
    elif p.direction == 2:
      if p.y != len(self.matrix) - 1:
        if self.at(p.x, p.y + 1) is None:
          self.movePlayerAt(p, p.x, p.y + 1)
          return 'You successfully moved south'
    elif p.direction == 3:
      if p.x != 0:
        if self.at(p.x - 1, p.y) is None:
          self.movePlayerAt(p, p.x - 1, p.y)
          return 'You successfully moved west'

    return 'You could not move'

  # TODO Handle doors and walls
  def playerLook(self, p):
    vision = self.linearCollisionFrom(p.x, p.y, p.direction)
    if vision is None:
      return 'You only see dust and rubbles'
    elif type(vision) is Player:
      return 'You see ' + vision.name + ' moving in the shadow'
    elif type(vision) is Door:
      return 'You see ' + if vision.isOpened: 'an opened door' else: 'a closed door'
    elif type(vision) is Wall:
      return 'You see a marvelously crafted wall'

  # TODO Handle doors and walls
  def playerShoot(self, p):
    if p.shoot():
      collision = self.linearCollisionFrom(p.x, p.y, p.direction)
      if collision is None:
        return 'You successfully hit nothing'
      elif isinstance(collision, Player):
        collision.hurt(p.name)
        return 'You hit ' + collision.name
    else:
      return 'Your weapon is empty'

  def movePlayerAt(self, p, x, y):
    self.matrix[p.y][p.x] = None
    self.matrix[y][x] = p
    p.x = x
    p.y = y

  def linearCollisionFrom(self, x, y, dir):
    if dir == 0 and y != 0:
      for i in range(y - 1, 0, -1):
        if self.at(x, i) is not None:
          return self.at(x, i)
    elif dir == 1 and x != len(self.matrix[y]) - 1:
      for i in range(x + 1, len(self.matrix[y]) - 1):
        if self.at(i, y) is not None:
          return self.at(i, y)
    elif dir == 2 and y != len(self.matrix) - 1:
      for i in range(y + 1, len(self.matrix) - 1):
        if self.at(x, i) is not None:
          return self.at(x, i)
    elif dir == 3 and x != 0:
      for i in range(x - 1, 0, -1):
        if self.at(i, y) is not None:
          return self.at(i, y)
    return None
    
  def at(self, x, y):
    return self.matrix[y][x]