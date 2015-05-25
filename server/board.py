from player import Player
from tile import Tile
from wall import Wall
from door import Door
import random

class Board:
  def __init__(self, x, y):
    self.spawners = []
    self.matrix = [[None for _ in range(y)] for _ in range(x)] 
    with open('map' + str(y) + str(x), 'r') as mapFile:
      for i, line in enumerate(mapFile):
        for j, tile in enumerate(line):
          if tile != '\n':
            self.matrix[i][j] = self.parseTile(tile)
            if tile is 's':
              self.spawners.append({ 'x':j, 'y':i })

    self.printBoard()

  def parseTile(self, char):
    return {
      '0': Tile(),
      's': Tile(),
      'i': Wall(),
      'd': Door()
    }[char]

  def printBoard(self):
    for y in range(len(self.matrix)):
      line = ''
      for x in range(len(self.matrix[y])):
        line += self.matrix[y][x].toChar() + ' '
      print(line)
    print('\n')

  def addPlayer(self, player):
    index = random.randint(0, len(self.spawners) - 1)
    x = self.spawners[index]['x']
    y = self.spawners[index]['y']
    self.matrix[y][x].addEntity(player)
    player.x = x
    player.y = y

  def removePlayer(self, player):
    self.matrix[player.y][player.x].removeEntity(player);
    
  # TODO handle doors and walls
  def playerMove(self, p):
    if p.direction == 0:
      if p.y != 0:
        if self.at(p.x, p.y - 1).canMoveTo():
          self.movePlayerAt(p, p.x, p.y - 1)
          return 'You successfully moved north'
    elif p.direction == 1:  
      if p.x != len(self.matrix[p.y]) - 1:
        if self.at(p.x + 1, p.y).canMoveTo():
          self.movePlayerAt(p, p.x + 1, p.y)
          return 'You successfully moved east'
    elif p.direction == 2:
      if p.y != len(self.matrix) - 1:
        if self.at(p.x, p.y + 1).canMoveTo():
          self.movePlayerAt(p, p.x, p.y + 1)
          return 'You successfully moved south'
    elif p.direction == 3:
      if p.x != 0:
        if self.at(p.x - 1, p.y).canMoveTo():
          self.movePlayerAt(p, p.x - 1, p.y)
          return 'You successfully moved west'

    return 'You could not move there'

  # TODO Handle doors and walls
  def playerLook(self, p):
    return self.linearCollisionFrom(p.x, p.y, p.direction).getLookedMessage()

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
    self.matrix[p.y][p.x].removeEntity(p)
    self.matrix[y][x].addEntity(p)
    p.x = x
    p.y = y

  def linearCollisionFrom(self, x, y, dir):
    if dir == 0 and y != 0:
      for i in range(y - 1, 0, -1):
        if not self.at(x, i).canLookThrough():
          return self.at(x, i)
    elif dir == 1 and x != len(self.matrix[y]) - 1:
      for i in range(x + 1, len(self.matrix[y]) - 1):
        if not self.at(x, i).canLookThrough():
          return self.at(i, y)
    elif dir == 2 and y != len(self.matrix) - 1:
      for i in range(y + 1, len(self.matrix) - 1):
        if not self.at(x, i).canLookThrough():
          return self.at(x, i)
    elif dir == 3 and x != 0:
      for i in range(x - 1, 0, -1):
        if not self.at(x, i).canLookThrough():
          return self.at(i, y)
    return Tile() #TODO change it
  def at(self, x, y):
    return self.matrix[y][x]