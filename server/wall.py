class Wall:
  def __init__(self):
    # Allows the wall to be destroyed by bullets stronger than it's armor
    self.destroyable = False 
    # Allows Look to go through this wall but without great info
    self.canSeeThrough = False
    # The bullets damage soaked by the wall. The rest goes through
    self.armor = 100