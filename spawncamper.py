#!/usr/bin/python
import os
import client.utils as utils
from client.client import Client

def exit():
	raise SystemExit

def play():
	os.system('clear')
	print(' ====-_-= S P A W N | C A M P E R =-_-==== ')
	print('==    |                             |    ==')
	print('==    |         R U L E S           |    ==')
	print('==    |                             |    ==')
	print('==    |  1 - Shoot stuff            |    ==')
	print('==    |  2 - Reload when needed     |    ==')
	print('==    |  3 - Disconnect upon death  |    ==')
	print('==    |                             |    ==')
	print(' ====-=-===========================-=-==== ')
	name = utils.io().pyin('Your spawncamper name: ')
	#host = input('Spawncamper Server address: ')
	c = Client('127.0.0.1', 5017, name)
	c.start()

def main(screen=None):
	print('ok-----')
	print('')
	print(screen)
	utils.io().setScreen(screen)
	while True:
		action = utils.io.pyin('What to do: ')
		if action == 'exit':
			exit()
		elif action == 'play':
			play()
		else:
			print("I don't know...")

utils.io(main)
main()