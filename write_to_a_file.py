'''
http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
Take the code from the How To Decode A Website exercise
, and instead of printing the results to a screen,
write the results to a txt file. In your code,
just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.

'''

from bs4 import BeautifulSoup
import requests

def decoder():
    file_name = raw_input("Enter Filename to write to: ")
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "lxml")
    i = 0
    b = ""
    with open(file_name, 'w') as open_file:
        for article in soup.find_all('h2', class_='story-heading'):
            if article.string == None:
                pass
            else:

                open_file.write(b.encode('utf-8'))


if __name__ == '__main__':
    decoder()