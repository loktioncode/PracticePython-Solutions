'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types "exit"
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''
import random

quit = ""
num = random.randint(1, 10)
tries = 0
while quit != "exit":
    try:

        usr_response = (raw_input("I have generated a number, can you guess what it is? "))
        if usr_response == "exit":
            break

        usr_response = int(usr_response)
        if usr_response > num:
            print "Your guess is too high. Let's try this again. Type 'exit' to quit"
            tries += 1
        elif usr_response < num:
            print "Your guess is too low. Let's try this again. Type 'exit' to quit"
            tries += 1
        elif usr_response == num:
            tries += 1
            print "Your guess is just right. Goodbye. It took you %d attempt(s) to get it right" % tries
            break

    except ValueError:
        print "You need to enter a number or type 'exit' to quit."
