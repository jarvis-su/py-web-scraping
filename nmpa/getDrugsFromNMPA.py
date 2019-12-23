import urllib3
import json
def download(url):
    print('Downloading ', url)
    userAgent = 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; MI 9 Build/QKQ1.190825.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'
    userAgent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'
    AcceptLanguage ='zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    AcceptEncoding= 'gzip, deflate'
    Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

    Cookie = 'JSESSIONID=A58B0B1DC96828832B92EE91D9E92605.7; tuNQaYE2WCOr80S=O43ziCfC7BLZm.F5edsUL84qX_T8DekwZhjFvL0AXMCYWDFH2_2qqyIQwdLwjfJb; tuNQaYE2WCOr80T=4zC94ZgkJ7NBDRsPXe.HrtFd3tXcvwudE41SSD4iUqL2TMsVQSF_QZ8LinHlNDmqOg_SeNEwr7NLRVyTJ7tG81Q310tSQQPTX0GJJDgefw7pPhWCn2BTVLKZ.MM_8iydxo1hNiKsmf7t9C5h3dn5b0DwZgfFZIzR1Ji4dsQdfhFkYTG5rdPQUPR5Y9.SG8jXjtXLxhv98Jx9DkyPYf2HWMJSWhjZlSe1sjjzACwcCozHaqBCvc_6F9mVCbKTdW44GKor91iD_VU2yaig6LwIHC5lVS0hSMTZQVlYPRJiQPf9AdA'

    http = urllib3.PoolManager(num_pools=5, headers={'User-Agent': userAgent,'Accept - Language': AcceptLanguage,
                                                     'Accept-Encoding': AcceptEncoding ,'Accept':Accept,
                                                     'Proxy-Connection': 'keep-alive',
                                                     'Cache-Control': 'max-age=0',
                                                     'Cookie':Cookie})
    r = http.request('GET', url)
    print(r.status)
    html = r.data.decode()
    return html


if __name__ == '__main__':
    demoURL = 'http://mobile.nmpa.gov.cn/datasearch/QueryList?tableId=25&searchF=Quick%20SearchK&pageIndex=1&pageSize=1500'
    demoDetailUrl = 'http://mobile.nmpa.gov.cn/datasearch/QueryRecord?tableId=25&searchF=ID&searchK=109228'
    demoDetailUrl = 'http://mobile.nmpa.gov.cn/datasearch/QueryRecord?tableId=25&searchF=ID&searchK='

    for i in range(1,10):
        demoURL = 'http://mobile.nmpa.gov.cn/datasearch/QueryList?tableId=25&searchF=Quick%20SearchK&pageIndex='+str(i)+'&pageSize=1500'
        ss = download(demoURL)

        print(ss)
        data = json.loads(ss)
        for item in data:
            # searchK = item['COUNT']
            searchK = item['ID']
            print(item['CONTENT'])
            detailInfoJson = download(demoDetailUrl + str(searchK))
            detailInfo = json.loads(detailInfoJson)
            detailJson = '{'
            for detail in detailInfo:
                if detail['NAME'] != '注':
                    detailJson = detailJson + '"' + detail['NAME'] + '":"' + detail['CONTENT'] + '",'
            detailJson = detailJson[:-1]
            detailJson = detailJson + '}'
            print(detailJson)
            detailData = json.loads(detailJson)
            # print(item['CONTENT'])

