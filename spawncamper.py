#!/usr/bin/python
import os
from command import Command
from board import Board
from player import Player
from notificationStack import NotificationStack

me = Player("A player")
board = Board(7, 7)
board.addPlayer(me, 0, 0)
stack = NotificationStack()
commands = { 
	"view": Command("view", "Look out for ennemies in front of you.", board.view), 
	"turn left": Command("turn left", "Turn to your left.", lambda: me.turn(-1)),
	"turn right": Command("turn right", "Turn to your right.", lambda: me.turn(1))
}

while True:
	os.system('clear')
	board.printBoard()
	stack.printStack()
	action = input("What to do: ")
	if action in commands:
		commands.get(action).action()
		action = input("")