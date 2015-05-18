import client.utils as utils

class NotificationStack:
  def __init__(self, size):
    self.size = size
    self.stack = [''] * self.size
    self.len = 0
    self.index = 0

  def add(self, msg):
    self.len = self.len + 1 if self.len < self.size else self.size
    self.stack[self.index] = msg
    self.index = (self.index + 1) % self.size

  def printStack(self):
    for msg in self.stack:
      utils.std.pyout(msg)