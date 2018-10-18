"""
ROCK PAPER SCISSORS
Do you really need further instructions?
Author: Wesley Applequist
"""

#from module import function
from random import randint

#options list
option = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie" : "Yawn, it's a tie!",
  "won" : "Yay, you won!",
  "lost" : "Aww, you lost!"
}

#Decides the winner
def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("And I selected: %s" % computer_choice)
  #CHECK FOR A TIE
  if user_choice == computer_choice:
  	print message["tie"]
  #CHECK ROCK AGAINST SCISSORS
  elif user_choice == option[0] and computer_choice == option[2]:
    print message["won"]
  #CHECK PAPER AGAINST ROCK
  elif user_choice == option[1] and computer_choice == option[0]:
    print message["won"]
  #CHECK SCISSORS AGAINST PAPER
  elif user_choice == option[2] and computer_choice == option[1]:
    print message["won"]
  #IN ALL OTHER CASES
  else:
   	print message["lost"]

#Prompts user for RPS choice
def play_RPS ():
	user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
	user_choice = user_choice.upper()
	computer_choice = option[randint(0,2)]
	decide_winner(user_choice, computer_choice)

#Call the function to start the game
play_RPS()