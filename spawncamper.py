#!/usr/bin/python
import os
from command import Command
from board import Board

board = Board(7, 7)
view = Command("view", "Look out for ennemies in front of you.", board.)
while True:
	os.system('clear')
	board.printBoard()
	action = input("What to do ?")