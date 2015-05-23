class Door:
  def __init__(self):
    self.destroyable = False 
    self.isOpened = False
    self.armor = 100

  def open(self):
    self.isOpened = true

  def close(self):
    self.isOpened = false