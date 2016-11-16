'''
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user.
    If not, print a different appropriate message.

'''

def odd_even():
    num = int(raw_input("Enter a number: "))
    if num % 2 != 0:
        print "%d is an odd number." % num

    if num % 4 == 0:
        print "%d is a multiple of 4." % num

    else:
        print "%d is an even number." % num

def calculator():
    usr_num = int(raw_input("Enter a number to check: "))
    check = int(raw_input("Enter a number to divide by: "))

    if usr_num % check == 0:
        print "%d divides evenly into %d" % (check, usr_num)
    else:
        print "%d does not divide evenly into %d" % (check,usr_num)

if __name__ == "__main__":
    calculator()
