import  urllib.request as httprequest
import re
def gettext(url):
    datapage=httprequest.urlopen(url)
    html=datapage.read()
    html=html.decode('utf-8')
    print(html)

def choice_content(html):
    reg=r'(class="article-con").+(div)'
    

def save_file(str):
    pass

url='http://www.2018box.com/book/595266?page=3'
choice_content(gettext(url))
