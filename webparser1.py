import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx =  ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter a url")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

numList = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    numList.append(tag.contents[0])

sum  = 0
for i in numList:
    num = int(i)
    sum = sum + num
print(sum)
