'''
Write a program (using functions!) that asks the user for a
long string containing multiple words. Print back to the user the
same string, except with the words in backwards order. For example,
 say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
'''

def string_reverse():
    usr_str = "My name is Michele"
    reverse_str = " ".join(usr_str.split()[::-1])
    print reverse_str

def string_reverse_2():
    usr_str = "My name is Michele"
    y = usr_str.split()
    result = []
    for word in y:
        result.insert(0,word)
    print " ".join(result)

if __name__ == "__main__":
    string_reverse_2()