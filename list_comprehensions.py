'''
Let's say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even
elements of this list in it.
'''

__author__ = 'terrameijar'

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers =   [elem for elem in a if elem % 2 == 0]



