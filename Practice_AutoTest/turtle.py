# -*- coding: utf-8 -*-
class Turtle:
    # 属性
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"

    # 方法
    def clib(self):
        print("爬！！！")
    def run(self):
        print("跑！！！")
    def bite(self):
        print("咬！！！")
    def eat(self):
        print("吃！！！")
    def sleep(self):
        print("睡！！！")

if __name__ == '__main__':
    Turtle().clib()
