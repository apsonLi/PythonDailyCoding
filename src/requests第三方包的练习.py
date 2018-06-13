import requests  
from bs4 import BeautifulSoup  
import re  
import os.path
import lxml
def getpage(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'  
    headers = {'User-Agent': user_agent}
          
    session = requests.session()
    
    page = session.get(url, headers=headers)
    
    soup = BeautifulSoup(page.text,'lxml')  #这里没有装lxml的话,把它去掉用默认的就好  
    
    return soup

def getiplist(taglist):
     iplist=[]
     prolist=[]
     for each in taglist:
         tdlist=each.find_all('td')#查找每个tr标签下的所有的td标签
         iplist.append(tdlist[1].string+':'+tdlist[2].string)
         prolist.append(tdlist[5].string)
     proxydict=dict(zip(prolist,iplist))#合成字典 目前问题在于 只能一个个的返回
     print(proxydict)


   
 
    
def saveiplist(iplist):
    for each in iplist:
        with open('iplist.txt','w')as f:
            f.write(each)
    
if __name__=='__main__':
    #匹配带有class属性的tr标签
    url="http://www.xicidaili.com/nn/1"
    
    soup=getpage(url)
    taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
    getiplist(taglist)







