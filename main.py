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
# print(thislist[-1:-4]) #这个例子说明 只能前向不能反向 想要从后往前遍历就不行
# print(len(thislist))
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist[-1])
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-2:-5])
# thistuple = ('test0','test1','test2','test3')
# thistuple[0] = 'aaa'
# print(thistuple)

# thisset = {"apple", "banana", "cherry"}
# print(type(thisset))
# print(thisset)
# print(thisset[0])

thisdict =	{
  "brand": "Porsche",
  "brand": "122",
  "model": "911",
  "year": 1963,
  "sah" :  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
}
# print(thisdict)
# print(thisdict["brand"])
# print(len(thisdict))
# for x in thisdict:
#   print(thisdict[x])
# for x ,y in thisdict.items():
#     print(x,y)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)
# def my_function(fname):
#   print(fname + " Gates")
#
# my_function("Rory John")
# my_function("Jennifer Katharine")
# my_function("Phoebe Adele")

# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)
# def myfunction(number):
#     number = 10
#     print(number)
#
# num = 100
# myfunction(num)
# print(num)
#
# def myfunction(number):
#     print('this is a function    ' + str(number))
#
# myfunction(5)
# def pass_value(number):
#     number = 10
#     return number
#
# test_number = 100
#
# test_number = pass_value(test_number)
#
# print(test_number)

# def pass_value(number):
#     number[0] = 1
#
# test_num = 10
# packet = [test_num]
# pass_value(packet)
#
# print(packet[0])

# def myfunc(count = "count"):
#     print(count)
# myfunc(1)
# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Phoebe", "Jennifer", "Rory")

# def swap(num1,num2):
#     num3 = num2
#     num2 = num1
#     num1 = num3
#
# count1 = 1
# count2 = 2
# swap(count1,count2)
# print(count1,count2)

# def fib(n):
#         if (n <= 1):
#             return n
#         else:
#             return fib(n-1) + fib(n-2)
# print(fib(3))

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# 使用 Person 来创建对象，然后执行 printname 方法：

x = Person("Bill", "Gates")
x.printname()