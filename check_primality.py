'''
Ask the user for a number and determine whether the number is prime or not.
'''
num = int(raw_input("Enter a number to check: "))
a = [number for number in range(2, num) if num % number == 0]

def is_prime(n):
    if num > 1:
        if len(a) == 0:
            print "Prime"
        else:
            print "Not a prime"
    else:
        print "Not a prime"

is_prime(num)
