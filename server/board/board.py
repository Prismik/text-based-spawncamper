from . tile import Tile
from . wall import Wall
from . door import Door
import random

class Board:
  def __init__(self, x, y):
    self.spawners = []
    self.matrix = [[None for _ in range(x)] for _ in range(y)] 
    with open('map' + str(x) + str(y), 'r') as mapFile:
      for i, line in enumerate(mapFile):
        for j, tile in enumerate(line):
          if tile != '\n':
            self.matrix[j][i] = self.parseTile(tile)
            if tile is 's':
              self.spawners.append({ 'x':j, 'y':i })
    
    self.linkTilesTogether()
    self.printBoard()
  
  def parseTile(self, char):
    return {
      '0': Tile(True, True, '0', 'A tile'),
      's': Tile(True, True, 's', 'A spawner'),
      'i': Wall(),
      'd': Door()
    }[char]

  def linkTilesTogether(self):
    for y in range(len(self.matrix)):
      for x in range(len(self.matrix[y])):
        self.createLinksForTileAt(x, y)

  def createLinksForTileAt(self, x, y):
    tile = self.at(x, y)
    # north
    if y != 0:
      link = self.at(x, y - 1)
      if type(link) is Tile:
        tile.linkedTiles.add(link)
    # north-east
    if y != 0 and x != len(self.matrix[y]) - 1:
      link = self.at(x + 1, y - 1)
      if type(link) is Tile:
        tile.linkedTiles.add(link)
    # east
    if x != len(self.matrix[y]) - 1:
      link = self.at(x + 1, y)
      if type(link) is Tile:
        tile.linkedTiles.add(link)
    # south-east
    if y != len(self.matrix) - 1 and x != len(self.matrix[y] - 1:
      link = self.at(x + 1, y + 1)
      if type(link) is Tile:
        tile.linkedTiles.add(link)
    # south
    if y != len(self.matrix) - 1:
      link = self.at(x, y + 1)
      if type(link) is Tile:
        link.linkedTiles.add(link)
    # south-west
    if y != len(self.matrix) - 1 and x != 0:
      link = self.at(x - 1, y + 1)
      if type(link) is Tile:
        link.linkedTiles.add(link)
    # west
    if x != 0:
      link = self.at(x - 1, y)
      if type(link) is Tile:
        link.linkedTiles.add(link)
    # north-west
    if y != 0 and x != 0:
      link = self.at(x - 1, y - 1)
      if type(link) is Tile:
        link.linkedTiles.add(link)

  def printBoard(self):
    for y in range(len(self.matrix)):
      line = ''
      for x in range(len(self.matrix[y])):
        line += self.at(x, y).toChar() + ' '
      print(line)

    print('\n')

  def addPlayer(self, player):
    index = random.randint(0, len(self.spawners) - 1)
    x = self.spawners[index]['x']
    y = self.spawners[index]['y']
    self.at(x, y).addEntity(player)
    player.x = x
    player.y = y

  def removePlayer(self, player):
    self.at(x, y).removeEntity(player);
    
  def tileCoordsInFrontOfPlayer(self, p):
    if p.direction == 0:
      if p.y != 0:
        return (p.x, p.y - 1)
    elif p.direction == 1:  
      if p.x != len(self.matrix[p.y]) - 1:
        return (p.x + 1, p.y)
    elif p.direction == 2:
      if p.y != len(self.matrix) - 1:
        return (p.x, p.y + 1)
    elif p.direction == 3:
      if p.x != 0:
        return (p.x - 1, p.y)

    return None

  def playerMove(self, p):
    coordsInFront = self.tileCoordsInFrontOfPlayer(p)
    if coordsInFront is not None:
      if self.at(coordsInFront[0], coordsInFront[1]).canMoveTo():
        self.movePlayerAt(p, coordsInFront[0], coordsInFront[1])
        if p.direction == 0:
          return 'You successfully moved north'
        elif p.direction == 1:
          return 'You successfully moved east'
        elif p.direction == 2:
          return 'You successfully moved south'
        elif p.direction == 3:
          return 'You successfully moved west'

    return 'You could not move there'

  def playerLook(self, p):
    return self.linearCollisionFrom(p.x, p.y, p.direction).describe()

  def playerShoot(self, p):
    if p.shoot():
      collision = self.linearCollisionFrom(p.x, p.y, p.direction)
      collision.hurt(p.name, 100)
      return 'You hit something'
    else:
      return 'Your weapon is empty'

  def playerOpen(self, p):
    coordsInFront = self.tileCoordsInFrontOfPlayer(p)
    if coordsInFront is not None:
      tile = self.at(coordsInFront[0], coordsInFront[1])
      if type(tile) is Door:
        return tile.open()

    return 'What are you trying to open?'

  def playerClose(self, p):
    coordsInFront = self.tileCoordsInFrontOfPlayer(p)
    if coordsInFront is not None:
      tile = self.at(coordsInFront[0], coordsInFront[1])
      if type(tile) is Door:
        tile.close()
        return 'You have closed a door'

    return 'What are you trying to close?'

  def movePlayerAt(self, p, x, y):
    self.at(p.x, p.y).removeEntity(p)
    self.at(x, y).addEntity(p)
    p.x = x
    p.y = y

  def linearCollisionFrom(self, x, y, dir):
    if dir == 0 and y != 0:
      for i in range(y - 1, -1, -1):
        if not self.at(x, i).canLookThrough():
          return self.at(x, i)
    elif dir == 1 and x != len(self.matrix[y]):
      for i in range(x + 1, len(self.matrix[y])):
        if not self.at(i, y).canLookThrough():
          return self.at(i, y)
    elif dir == 2 and y != len(self.matrix):
      for i in range(y + 1, len(self.matrix)):
        if not self.at(x, i).canLookThrough():
          return self.at(x, i)
    elif dir == 3 and x != 0:
      for i in range(x - 1, -1, -1):
        if not self.at(i, y).canLookThrough():
          return self.at(i, y)

    return Tile(True, True, '0', 'You only see dust and rubbles') #TODO change it

  def at(self, x, y):
    return self.matrix[x][y]
