
from urllib import request
def download(url):
   ss = request.urlopen(url).read().decode()
   print(ss)


if __name__ == '__main__':
    url = 'http://example.webscraping.com'
    download(url)
