"""
This program adds the sum of two dice and asks the player to guess the sum. If the player is right, they win. If they are wrong, they lose.
Author: Wesley Applequist
"""

##GAME TIME
dice_roll(24)

##IMPORTS
#from module import function
from random import randint
from time import sleep

##FUNCTIONS
#Prompt the player for their guess
def get_player_guess():
  guess = int(raw_input("Enter what you think the sum will be: "))
  return guess

#Roll the dice
def dice_roll(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum possible value is %d" % (max_val))
  guess = get_player_guess()
  if guess > max_val:
    print("Your guess is greater than the maximum value. Exiting...")
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %d" % first_roll)
    sleep(1)
    print("The second roll is %d" % second_roll)
    sleep(1)
    total = first_roll + second_roll
    print("The total is %d" % total)
    print("Result...")
    sleep(1)
    if guess == total:
      print("You win!")
    else:
      print("You lost!")