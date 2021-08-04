# -*- coding: UTF-8 -*-
# import requests
# import json
#
# url = 'http://www.baidu.com'
# url = 'http://www.baidu.com？id=1001'
# #params : 参数为字典或字符串
# params = {'id':1001}
# params = {'id':[1001,1002]}
# params = {'id':"1001,1002"}  #浏览器解析会将逗号解析成 %2c
# response = requests.get(url=url,params=params)
#
# print(response.status_code)
# print (response.url)
#
# #请求url
# requests.post()
#请求headers
# headers = {"Content-Type":"appliaction/json"}
# URL = 'i love you'
# print (URL[2])
#请求json
import requests

# url = 'http://www.baidu.com'
# g = requests.get(url)
# g.encoding = 'utf-8'
# print(g.encoding)
# print(g.text)
# #返回的是字典对象
# print (g.cookies)

url_image = 'https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/searchbox/nicon-2x-6258e1cf13.png'

image = requests.get(url_image)
with open("./baidu.png","wb") as f:
    f.write(image.content)
