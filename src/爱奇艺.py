from bs4 import BeautifulSoup
import requests
import re
import database
import time
import demjson
#coding=utf-8

def get_html(url):
    response=requests.get(url)
    html=response.text#在这里使用response.content 也一样但是有的网页需要转码
    return html

def bstask(html):
    soup=BeautifulSoup(html,'html.parser')
    newest=soup.select('.site-piclist_pic_link ')
    #a=type(list1[0])
    db = database.DB()
    for x in newest:
        title = (x['title'])
        if not db.select(title,'video'):#判断是否有相同的数据
            img = (x.img['src'])#将数据从dict中遍历出来
            url = (x['href']+'\n')
            douban_info =get_douban_info(title)
            keywords = douban_info['keywords']
            desc = douban_info['desc']
            is_vip = 0
            pv = 0
            score = 0 
            status = 0
            add_time = (int)(time.time())
            # print(title, keywords, desc, img, url, is_vip, pv, status, add_time, score)
            db.write_video(title, keywords, desc, img, url, is_vip, pv, status, add_time, score)#存入数据库
       

def get_douban_info(title):
    db = database.DB()
    search_id_url = 'https://api.douban.com/v2/movie/search?q='+title #豆瓣的影片搜索接口，但是缺少影片的简介和关键字信息，我必须先把豆瓣中的影片id
    time.sleep(1.5)#公共接口1分钟只能访问40次
    search_id_html=get_html(search_id_url)#爬虫获取json
    search_id_text = demjson.decode(search_id_html)#将json字符串解析成dict对象
    subjects = (search_id_text['subjects'])
    for item in subjects:
        douban_id = item['id']#获得豆瓣的影片id
        douban_title = item['original_title']
        
        search_info_url ='https://api.douban.com/v2/movie/subject/'+douban_id #豆瓣的影片信息接口,必须给它穿豆瓣的影片id，才能查询
        time.sleep(1.5)
        search_info_html = get_html(search_info_url)
        search_info_text = demjson.decode(search_info_html)
        keywords = search_info_text['genres']
        desc = search_info_text['summary']
        if not db.select(douban_title,'douban_id'):
            #print(item['id']+' '+item['original_title'])
            db.write_douban_id(douban_title,douban_id,keywords,desc)#将数据存进数据库 ，万一以后要用呢
    return {'desc':desc , 'keywords':keywords}
    

#url='http://www.iqiyi.com/dianying_new/i_list_paihangbang.html'
#db = database.DB()

#bstask(html)





