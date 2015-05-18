import curses
import curses.textpad as textpad
import time
import threading

class NixInputHandler:
  def __init__(self, screen):
    self.win = screen
    self.row = 0
    self.terminated = False
    self.win.nodelay(True) # non-blocking getch
    self.win.keypad(True)
    curses.cbreak() # no line buffering
    self.win.keypad(1);
    curses.noecho()
    # self.win.addstr('Playing on a Unix sytem')

  def kbhit(self):
    ch = self.win.getch()
    if (ch != -1):
      curses.ungetch(ch)
      return 1
    else:
      return 0

  def pyin(self, prompt=None):
    #textpad.Textbox(self.win).edit()
    if prompt:
      self.win.addstr(prompt)
    text = self.win.getstr()

    #return text
    result = []
    while True:
      if self.kbhit() == 1:
        result.append(self.win.getch())
        if result[-1] in ['\r', '\n']:
          self.win.addstr('')
          return ''.join(result).rstrip()
      if self.terminated:
        return None
      time.sleep(0.1)  # just to yield to other processes/threads

  def pyout(self, msg):
    self.win.addstr(0, self.row, msg)
    self.row += 1

  def clear(self):
    self.win.clear()
    self.row = 0