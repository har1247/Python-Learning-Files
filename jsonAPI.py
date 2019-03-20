import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key=False

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if api_key is False:
    api_key = 42
    serviceurl ="http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl ="http://py4e-data.dr-chuck.net/json?"


while True:
    address = input("Enter a address: ")
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving url ", url)

    html = urllib.request.urlopen(url, context = ctx).read().decode()
    print('Retrieved', len(html), 'characters')

    try:
        js = json.loads(html)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    placeid = js['results'][0]['place_id']
    print(placeid)

    #out= json.dumps(js, indent=4)
    #print(out)‹›

    # Another way --
    # count = 0
    # for i in js['results']:
    #     if count>0:
    #         break
    #     print(i['place_id'])
    #     count +=1
