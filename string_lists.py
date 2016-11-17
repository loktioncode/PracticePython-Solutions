'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
def is_palindrome():

    palindrome = raw_input("Enter a word to check ")
    left = 0
    right = len(palindrome)

    while left < right:
        if palindrome[left]!= palindrome[right - 1]:
            print "Not Palindrome"
            quit()
        left += 1
        right -= 1
    print "Palindrome"

if __name__ == "__main__":
    is_palindrome()
