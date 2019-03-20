import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ')
position = input("Enter a position")
repeat = input("Enter count")
try:
    pos = int(position)
    i = int(repeat)
except:
    print("Invalid position or count")
    sys.exit()

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


while i >=1:
    count = 1
    tags = soup('a')
    for tag in tags:
        if count == pos:
            print(tag.get('href', None))
            u = tag.get('href', None)
            html = urllib.request.urlopen(u).read()
            soup = BeautifulSoup(html, 'html.parser')
        count = count + 1
    i = i - 1
