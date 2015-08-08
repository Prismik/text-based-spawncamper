#!/usr/bin/python
import os
import client.utils as utils
from client.client import Client

def exit():
  raise SystemExit

def play():
  utils.std.clear()
  utils.std.pyout(' ====-_-= S P A W N | C A M P E R =-_-==== ')
  utils.std.pyout('==    |                             |    ==')
  utils.std.pyout('==    |         R U L E S           |    ==')
  utils.std.pyout('==    |                             |    ==')
  utils.std.pyout('==    |  1 - Shoot stuff            |    ==')
  utils.std.pyout('==    |  2 - Reload when needed     |    ==')
  utils.std.pyout('==    |  3 - Disconnect upon death  |    ==')
  utils.std.pyout('==    |                             |    ==')
  utils.std.pyout(' ====-=-===========================-=-==== ')
  name = utils.std.pyin('Your spawncamper name: ')
  #host = input('Spawncamper Server address: ')
  c = Client('127.0.0.1', 5000, name)
  c.start()

def main(screen=None):
  utils.io('Basic')
  utils.std.clear()
  while True:
    action = utils.std.pyin('What to do: ')
    if action == 'exit':
      exit()
    elif action == 'play':
      play()
    else:
      utils.std.pyout("I don't know...")

# curses.wrapper(main) # FOR CURSES MODE
main()