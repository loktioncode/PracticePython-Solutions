'''
Use the BeautifulSoup and requests Python packages to print out a list
of all the article titles on the New York Times homepage.
'''

from bs4 import BeautifulSoup
import requests

def decoder():
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "lxml")
    i = 0
    for article in soup.find_all('h2', class_='story-heading'):
        if article.string == None:
            pass
        else:
            i += 1
            print str(i) + ':', article.string.strip() +'\n'



if __name__ == '__main__':
    decoder()