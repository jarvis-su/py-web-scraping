import urllib3
def download(url):
    print('Downloading ', url)
    http = urllib3.PoolManager(num_pools=5, headers={'User-Agent': 'wswp'})
    r = http.request('GET', url)
    print(r.status)
    html = r.data.decode()

    return html


if __name__ == '__main__':
    url = 'http://example.webscraping.com'
    ss = download(url)
    print(ss)
