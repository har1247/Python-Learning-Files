import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter a path: ")
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
results = tree.findall('comments/comment')
count = 0

for item in results:
    count =  count + int(item.find('count').text)
print(count)
