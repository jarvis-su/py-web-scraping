import requests

url = 'https://www.amazon.cn/dp/1408856778?_encoding=UTF8&ref_=pc_cxrd_658390051_recTab_658390051_t_8&pf_rd_p=7e00fee6-4e12-48f0-b4af-b99068b52067&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=658390051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=JJAA5P201AAYNF7B6R7V&pf_rd_r=JJAA5P201AAYNF7B6R7V&pf_rd_p=7e00fee6-4e12-48f0-b4af-b99068b52067'

def getText(url):
    print('##########################################################################')
    try:
        r = requests.get(url)
        print(r.request.headers)
        r.raise_for_status()
        print(r.headers)
        print(r.status_code)
        print(r.text[:1000])
    except:
        print('failed ')


def getText1(url):
    print('##########################################################################')
    try:
        kv = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv)
        print(r.request.headers)
        print(r.status_code)
        r.raise_for_status()
        print(r.text[:1000])
    except:
        print('failed')

if __name__ == '__main__':
    getText(url)
    getText1(url)