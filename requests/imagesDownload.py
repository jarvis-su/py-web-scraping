import requests
import os

path = 'D://resources//temp//'
def getImage():
    url = 'http://image.nationalgeographic.com.cn/2018/0102/20180102104744349.jpg'
    fileName = path + url.split('/')[-1]
    print(fileName)
    try:
        r = requests.get(url)
        print(r.status_code)
        storeFile(path, fileName, r.content)
        print('image has been downloaded succefully')
    except:
        print('failed')

def storeFile(path, fileName, fileContext):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(fileName):
            with open (fileName,'wb') as f:
                f.write(fileContext)
                f.close()
                print('file has been stored succefully')
    except:
        print('File has not been stored succefully')

if __name__ == '__main__':
    getImage()