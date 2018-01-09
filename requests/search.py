import  requests

def baiduSearch():
    kv = {'wd':'Python'}
    url = 'https://www.baidu.com/s'
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        print(r.status_code)
        print(r.request.url)
        print(len(r.text))
        print(r.text[:10000])
    except:
        print('failed')

if __name__ == '__main__':
    baiduSearch()