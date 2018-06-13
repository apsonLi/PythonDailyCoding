#coding=utf-8
import requests
import re 

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" width'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

def getImglist():
    imglist=[]
    address1='http://www.j-onepiece.com/images/stmn'
    address2='.jpg'
    for i in range(1,7):
        imglist.append(address1+str(i)+address2)
    return imglist

def save_Img(imglist):
    count=0
    if imglist!= None:
        for each in imglist:
            response=requests.get(each)
            img=response.content
            filename=str(count)+'.jpg'
            count+=1
           
            with open(filename,'wb') as f:
                f.write(img)


    
a=getImglist()
save_Img(a)
