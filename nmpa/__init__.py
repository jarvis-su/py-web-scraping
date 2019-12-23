demoURL = 'http://mobile.nmpa.gov.cn/datasearch/QueryList?tableId=25&searchF=Quick%20SearchK&pageIndex=1&pageSize=15'
demoDetailUrl='http://mobile.nmpa.gov.cn/datasearch/QueryRecord?tableId=25&searchF=ID&searchK=109228'


import urllib3
def download(url):
    print('Downloading ', url)
    http = urllib3.PoolManager(num_pools=5, headers={'User-Agent': 'wswp'})
    r = http.request('GET', url)
    print(r.status)
    html = r.data.decode()

    return html


if __name__ == '__main__':
    url = demoURL
    ss = download(url)
    print(ss)
