'''
Write a password generator in Python. Be creative with how you generate passwords
- strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a
 new password every time the user asks for a new password. Include your
 run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be.
     For weak passwords, pick a word or two from a list.

'''


import random

passwd_length = int(raw_input("Password length: "))

pwd_sample = "abcdefghijklmnopqrstuvABCDEFGHIJKLMN" \
             "OPRQSTUVWXZ1234567890!@#$%^&*()_+="

new_passwd = random.sample(pwd_sample, passwd_length)
print "".join(new_passwd)

