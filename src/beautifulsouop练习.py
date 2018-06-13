from bs4 import BeautifulSoup
import urllib.request

def pages(url):
    pagelist=[]
    for i in range(1,10):
        nextpage=url+'?page='+str(i)
        pagelist.append(nextpage)
    return pagelist

def save_file(content):
    with open('a.txt','ab+') as f:
        f.write((content).encode('utf-8'))
    f.close()
    
def get_html(pagelist):
    for each in pagelist:
        
        page=urllib.request.urlopen(each)

        html=page.read()
        
        soup =BeautifulSoup(html,'html.parser')

        html_all_text=(soup.get_text())#获取html中的所有文字内容

        
        save_file(html_all_text)


url='http://www.2018box.com/book/603851'

list=pages(url)
get_html(list)
#.con .wrap .pin_view .pin-view-wrapper .main-part subground .article-con

#print(html_all_text)
