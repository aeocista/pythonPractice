#!/usr/python

### Battleship ###

# import
from random import randint

# Set up a blank board
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

# Print the board
print_board(board)

# Set your battleship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# For "debugging"
print ship_row
print ship_col

# Now the game begins...
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
  print "You missed my battleship!"
  guess_row = "X"
  guess_col = "X"
  print_board(board)
  