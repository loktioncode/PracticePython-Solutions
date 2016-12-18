'''
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns
(then prints) an appropriate boolean.

Extras:

    Use binary search.

'''


def element_search(x, y):
    if y in x:
        return True
    else:
        return False

list_of_numbers = (raw_input("Enter list ")
extra_number = raw_input("Enter an extra number ")

print element_search(list_of_numbers, extra_number)