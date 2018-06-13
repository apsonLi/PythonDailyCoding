import requests
from bs4 import BeautifulSoup
import lxml
def getHtml(url):
    Useragent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    
    headers={'User-Agent':Useragent}
    
    Session=requests.session()
    
    Page=Session.get(url,headers=headers)
    
    soup=BeautifulSoup(Page.text,'lxml')

    content=soup.select('.article-con')
    
    return content

def get_page_content(content):
    print(content[0].get_text())


if __name__ =='__main__':
    url=str(input('请输入url'))
    
    soup= getHtml(url)
    
    get_page_content(soup)
