import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =  input("Enter a url")
html = urllib.request.urlopen(url, context=ctx).read().decode()
info = json.loads(html)
count=0

for item in info['comments']:
    count +=  int(item['count'])
print(count)
