import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p["class"])
print(soup.a)