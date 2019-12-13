# print("hello! word! \n" * 8)

# temp = input("输入：")
# guess = int(temp)
# if guess < 10:
#     print("YES:" + str(guess) + "小于 10!")
# elif 100 >= guess >= 10:
#     print("YES:" + str(guess) + "大于 10,小于100!")
# else:
#     print("YES:" + str(guess) + "大于 100!")

list1 = [1,2,3,4,5,5,6]
list2 = [7,8,9]
# #增加
# list1.append(list2)   #[1, 2, 3, 4, 5, 5, 6, [7, 8, 9]]
# list1.extend(list2)   #[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
# list1.insert(2,8)     #[1, 2, 8, 3, 4, 5, 5, 6]
# #删除
# list1.remove(3)       #[1, 2, 4, 5, 5, 6]
# list1.pop(0)          #[2, 3, 4, 5, 5, 6]
# list1.pop()           #[1, 2, 3, 4, 5, 5]
# del list1[0]          #[2, 3, 4, 5, 5, 6]
# print(list1)
print(list1[:])         #[1, 2, 3, 4, 5, 5, 6]
print(list1[1:3])       #[2, 3]
print(list1[2:])        #[3, 4, 5, 5, 6]
print(list1[:4])        #[1, 2, 3, 4]

print(list1.count(1))        #1

print(list1.index(1))
coll = {1,2,3,4,5,5,6}
print(coll)
# print(coll.)
# print(collection.reverse())
set1 = {1,2,3,4,5,6}
set2 = set((7,8,9))
set3 = set(range(1,4))
print("set3:",set3)

set4 = {num for num in range(1, 100) if num%10==0 and num%4==0}
print(set4)  #  {40, 80, 20, 60}

set5 = {num
for num in range(1,100)
     if num%10 == 0 and num%4 == 0
     }
print(set5)

tuple1 = (1,2,3,4,5,6)
print(tuple1)

str1 = "I fuck your mother!"
str2 = "i fuck your mother!"
print(str2.capitalize())
print(str1.casefold())

class Student():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __repr__(self):
        return "id:"+self.id,"name"+self.name

s1 = Student(1,"zhangsan")
print(s1.id,s1.name)

print("{0} love {1} {2}".format("I","eat","fish"))
print("{a} love {b} {c}".format(a="I",b="eat",c="fish"))
print('%c %c %c' % (50,60,80))

print("{} {}".format("hello","world") )
print("{0} {1} {0}".format("hello","or"))
person = {"name":"zhangsan","age":88}
print("My name is {name},I'm {age} years old!".format(name="zhangsan",age=88))
print("My name is {name},I'm {age} years old!".format(**person))

stu = ["opcai","linux","MySQL","Python"]
print("My name is {0[0]} , I love {0[1]} !".format(stu))

print("%d" % 3.1415)
print("%f" % 3.1415)

# print(help(list))

def my_first_function(name):
    print("形参……")
    print(name+"lallalalalal"+"实参")

if __name__ == '__main__':
    # print(my_first_function.__doc__)
    my_first_function.__doc__
    my_first_function("zhangsan")

# print(print.__doc__)

# help(print)

def test(*param,exp):
    print("参数长度：",len(param),"排除项：",exp)
    print("第二个参数是：",param[1])
    return param;

if __name__ == '__main__':
    t = test(1,2,3,4,5,exp=2)
    print(t)

golable_variable = 100
def test2(price,rate):
    a = price*rate
    return a

if __name__ == '__main__':
    b = test2(golable_variable,0.1)
    print(b)

def fun1():
    print("fun1")
    def fun2():
        print("fun2")
    fun2()

if __name__ == '__main__':
    fun1()

#匿名函数
t = lambda x,y : 2 * x + y  + 1
print(t(5,2))

def odd(x):
    return x % 2
temp = range(10)
print(list(list(temp)))
show = filter(odd,temp)
print(list(show))
print(9 % 2)

def factorial(num):
    result = num
    for i in range(1,num):
        result *= i
    return result

def factorial_2(n):
    if n == 1:
        return n
    else:
        return n * factorial_2(n-1)

if __name__ == '__main__':
    n = factorial(10)
    print(n)

    # number = int(input("请输入："))
    # result = factorial(number)
    # print("%d 的阶乘 %d:" % (number,result))
    #
    # number2 = int(input("请输入2："))
    # result2 = factorial(number)
    # print("%d 的阶乘 %d:" % (number, result2))

#裴波那切数列
def peibo(n):
    if n < 1 :
        print("输入错误！")
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return peibo(n-1)+peibo(n-2)

if __name__ == '__main__':
    print("裴波那切：",peibo(20))

x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

if __name__ == '__main__':
    addone('China')
    addone('Japan')
    addone('china')

    print(len(country_counter))

    confusion = {}
    confusion[1] = 1
    confusion['1'] = 2
    confusion[1] += 1
    print(confusion)

    sum = 0
    for k in confusion:
        sum += confusion[k]

    print(sum)

dict1 = {1:1,'1':2,"name":"sam","age":18}
print(dict1["name"])

import json
# print(json.dumps(dict1, encoding='UTF-8', ensure_ascii=False))
print(json.dumps(dict1))

dict2={}
# dict2 = dict2.fromkeys((1,2,3))
# dict2 = dict2.fromkeys((1,2,3),"100")
# dict2 = dict2.fromkeys((1,2,3),("one","two"))
dict2 = dict2.fromkeys(range(10),"啦")
print(json.dumps(dict2))

# !/usr/bin/python
# -*- coding: UTF-8 -*-
seq = ('Google', 'Runoob', 'Taobao')
dict = dict.fromkeys(seq)
print("新字典为 : %s" % str(dict))
dict = dict.fromkeys(seq, 10)
print("新字典为 : %s" % str(dict))


list_demo = []
list_demo2 = [1,2,3,4,5]
print(type(list_demo))
print(type(list_demo2))
dict_demo = {}
dict_demo3 = {1:2,3:4,5:6}
print(type(dict_demo))
print(type(dict_demo3))
set_demo = {}
set_demo2 = {1,2,3,4,5}
print(type(set_demo))
print(type(set_demo2))

num1 = [0,1,2,3,4,5,5,3,7]
print(list(set(num1)))

set_1 = {1,2,3,4,5,5,6,6,7}
print(2 in set_1)

# file = open("E:\\record.txt")
# print(file)
# # print(file.read())
# print(file.read(5))
# print(file.tell())
# print(file.seek(3))

#-*_coding:utf8-*-

#乱码问题
# import sys
# type = sys.getfilesystemencoding()
# print(mystr.decode('utf-8').encode(type))

# unicodePage = myPage.decode("gbk").encode('utf-8').decode('utf-8')

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# os.chdir("E:/")
# o = os.getcwd()
# o = os.listdir()
# o = os.listdir("E:\\")
# o = os.system('cmd')
# print(o)

import pickle
if __name__ == '__main__':
    my_list = [123, 455, 3.45, '小甲鱼', ['another list']]
    pickle_file = open("E:\\my_list.pkl","wb")
    pickle.dump(my_list,pickle_file)
    pickle_file.close()

    pickle_file = open("E:\\my_list.pkl","rb")
    my_list2=pickle.load(pickle_file)
    print("my_list2:",my_list2)

    try:
        f = open('我是一个文件.txt','w')
        print("f.write('存在！'):",f.write('存在！'))
        f.close()
    except (OSError,TypeError) as reason:
        print("错误！！！")
    finally:
        print("结束！！！")

    # try:
    #     s = None
    #     if s is None:
    #         print("s 是空对象")
    #         raise NameError  # 如果引发NameError异常，后面的代码将不能执行
    #     print(len(s))  # 这句不会执行，但是后面的except还是会走到
    # except TypeError:
    #     print("空对象没有长度")
    #
    # s = None
    # if s is None:
    #     raise NameError
    # print('is here?')  # 如果不使用try......except这种形式，那么直接抛出异常，不会执行到这里

print(11.1215 // 1)

# import easygui
# if __name__ == '__main__':
#     easygui.msgbox("Hell哦！！")

import time
time.sleep(1)
from Practice_AutoTest import turtle

if __name__ == '__main__':
    turtle.Turtle().clib()

class A:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

a = A('hello')
a.printname()

class  Person:
    __name = '小甲鱼'
    def getname(self):
        return self.__name

p = Person()
print(p.getname())
print(p._Person__name)




