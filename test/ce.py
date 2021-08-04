# -*- coding: UTF-8 -*-
import requests

response = requests.get('http://www.baidu.com')

print(response.text)
print('状态码:',response.status_code)

