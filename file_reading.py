'''
Exercise taken from http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
Given a .txt file that has a list of a bunch of names,
count how many of each name there are in the file, and print out the results to the screen.
Extra:

    Instead of using the .txt file from above (or instead of, if you want the challenge),
    take this .txt file[http://www.practicepython.org/assets/Training_01.txt], and count how many of each "category" of
     each image there are.
    This text file is actually a list of files corresponding to the SUN database scene recognition database,
    and lists the file directory hierarchy for the images.
     Once you take a look at the first line or two of the file, it will be clear which part represents
     the scene category.
'''

star_wars = {}
count = 0

with open('nameslist.txt', 'r') as names:
    for line in names.readlines():
        star_wars[line.strip()] = count
        count += 1


    for k, v in star_wars.iteritems():
        print k, 'appears', v, 'times'
