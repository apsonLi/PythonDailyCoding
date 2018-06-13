import urllib.request
response=urllib.request.urlopen('http://t1.b0b1.com/720/5b/5b5bd9b751dd0aac870a49fe7d0aa5d0c0333e7d.jpg')
cat_imag=response.read()
with open('cat.jpg','wb') as f:
    f.write(cat_imag)

    
