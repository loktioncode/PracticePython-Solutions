#Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number.
# (If you don't know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(raw_input("Enter number "))
divisors = []
num_list = range(1,num)
for item in num_list:
    if num % item == 0:
        divisors.append(item)

print "The list of all the divisors of %d is %r: " % (num , divisors)


