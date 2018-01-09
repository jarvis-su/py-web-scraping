import requests

url = 'https://item.jd.com/2538435.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    print(r.status_code)
    print(r.encoding)
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('exception')