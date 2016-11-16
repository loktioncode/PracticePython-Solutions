'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.


Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

#get the current year from OS
# get input from user (name, age)
# calculate how many years are left before the user turns 100 (100-current age)
#add difference to current year

#'''
#name = raw_input("What is your name? ")
#print "Hello %s.\n"
#age = int(raw_input("How old are you?"))
#'''

import time
now = int(time.strftime("%Y")) #Y option prints the year
name = raw_input("What is your name? ")
print "Hello %s " % name
age = int(raw_input("How old are you?"))
years_to_hundred = 100 - age
future_date = years_to_hundred + now
print "%s, you are %d years old. You will be a 100 years old in %d." %(name,age,future_date)
#print now



