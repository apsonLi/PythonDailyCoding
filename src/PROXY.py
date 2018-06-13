import urllib.request
import random
while 1:
    url='http://www.whatismyip.com.tw'
    iplist=['180.118.247.139:9000','121.8.98.197:80','95.128.181.120:3128','58.255.142.27:8118']
    proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

    opener=urllib.request.build_opener(proxy_support)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]

    urllib.request.install_opener(opener)

    response=urllib.request.urlopen(url)

    html=response.read().decode('utf-8')


    print (html)
                                             
