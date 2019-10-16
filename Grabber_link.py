import re, requests
from bs4 import BeautifulSoup
checkedUrls=[]
def processUrl(url):
 if not url in checkedUrls:
    try:
        if 'text/html' in requests.head(url).headers['Content-Type']:
            req=requests.get(url)
            if req.status_code==200:
                print(url)
                checkedUrls.append(url)
                html=BeautifulSoup(req.text,'html.parser')
                pages=html.find_all('a')
                for page in pages:
                    url=page.get('href')
                    processUrl(url)
    except:
        pass
url='http://kuttyweb.co'    //Put the url or url list 
processUrl(url)
for i in checkedUrls:
    print("externel urls:")
    print(i)
