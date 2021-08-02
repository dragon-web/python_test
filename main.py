# -*- coding: UTF-8 -*-
import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')
import requests

# response = requests.get('https://www.baidu.com/s?wd=iphone&rsv_spt=1')
# print(response.text)
# print ('\n')
# print(response.content)

# 可以将参数放到字典里面
#
# paras = {
#     'wd' : 'iphone',
#     'rsv_spt' : '1'
# }
# url1 = 'http://www.baidu.com'
# response = requests.get(url1,params=paras)

# print (response.text)

# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.url)

# a = "Hello, World!"
# b = a.split(",") # returns ['Hello', ' World!']
# print(b)

# txt = "China is a great country"
# x = "ina" not in txt
# print(x)
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# 列表（List）是一种有序和可更改的集合。允许重复的成员。
# 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
# 集合（Set）是一个无序和无索引的集合。没有重复的成员。
# 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。
# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "你好"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])