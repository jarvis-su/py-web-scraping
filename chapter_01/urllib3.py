import urllib3
def download(url):
    http = urllib3.PoolManager()
    # resp1 = http.request('GET',url, body=data)
    # resp2 = http.urlopen('GET',url, body=data)
    # print(resp2.data.decode())



if __name__ == '__main__':
    download('http://www.baidu.com')
