'''
Exercise taken from http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has a
list of all prime numbers under 1000, and the other .txt file
has a list of happy numbers up to 1000.
'''

with open('primenumbers.txt') as primes:
    prime_numbers = list(primes) #  This is == primes.readlines()
# list or readlines method adds a trailing \n, convert to int to remove this
prime_numbers = [int(number) for number in prime_numbers]

with open('happynumbers.txt') as happy:
    happy_numbers = happy.readlines()
happy_numbers = [int(number) for number in happy_numbers]

common_numbers = set(prime_numbers).intersection(happy_numbers)
print sorted(common_numbers)
