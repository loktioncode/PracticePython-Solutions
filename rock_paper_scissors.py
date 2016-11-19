
'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''
__author__ = 'terra'

import sys

user1 = raw_input("What is your name? ")
user2 = raw_input("And your name? ")

user1_play = raw_input("%s What's your play? Rock, Paper or Scissors? " % user1)
user2_play = raw_input("%s What's your play? Rock, Paper or Scissors? " % user2)

def compare(u1,u2):
    if u1 == u2:
        return ("It's a tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock Wins")
        else:
            return("Paper Wins")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors Wins")
        else:
            return("Rock Wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper Wins")
        else:
            return("Scissors Wins")
    else:
        return("Invalid Input, you have not entered rock, paper or scissors. Please try again.")
        sys.exit()

print compare(user1_play, user2_play)
