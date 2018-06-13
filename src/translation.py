import urllib.request
import urllib.parse
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data={}
data['type']='AUTO'
data['i']='name'

data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1516527253664'
data['sign']='cd90ab999f2f3d2ccefaa1483c5be10d'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')

req=urllib.request.urlopen(url,data)
html=req.read().decode('utf-8')

print(html)
