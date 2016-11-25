'''
Write a program (function!) that takes a list and
returns a new list that contains all the elements of the first list
minus all the duplicates.

Extras:

    Write two different functions to do this - one using a
    loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the
     solution for that in a different function.
'''

import unittest

class listTest(unittest.TestCase):
    test_list = [1,1,2,5,7,8,2,5]
    no_dupes_list = sorted([8,1,2,5,7])


    def test_new_list_returned_without_duplicates(self):
        # call list generator function and pass in a list with duplicates
        # assert that returned list has no duplicates
        # test_list = [1,1,2,5,7,8,2,5]
        self.assertEqual(list_gen(self.test_list), self.no_dupes_list)

    def test_new_list_returned_without_duplicates_using_loop(self):
        # call loop list generator function and pass in a list with duplicates
        # assert that returned list has no duplicates
        self.assertEqual(list_gen_loop(self.test_list), self.no_dupes_list)



def list_gen_loop(l):

    second_list = []
    for item in l:
        if item not in second_list:
            second_list.append(item)

    return second_list


def list_gen(l):
    return sorted(list(set(l)))


if __name__ == '__main__':
    unittest.main()
