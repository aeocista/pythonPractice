#!/bin/python

### Battle_Ship ###

# Making the board

board = []

for i in range(5):
  board.append(["O"]*5)

def print_board(board_in):
  for row in board_in:
    print row # was print " ".join(row) # What is " ".join(row) doing?

print_board(board)

