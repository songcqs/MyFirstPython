'''
  Code description： 继承基类，封装登陆页面所有的元素和元素的操作方法
  Create time：2018-11-16
  Developer：
'''
# -*- coding: utf-8 -*-
from DianqingOA_AutoTest.DianqingOA.test.models.base_page import BasePage
import xlrd                                    # excel操作相关的模块
from DianqingOA_AutoTest.DianqingOA.test.models.log import Logger
excelfile_path = r'D:\python-workspace\我的python程序\DianqingOA_AutoTest\DianqingOA\data\testdata\elementData.xlsx'
workbook = xlrd.open_workbook(excelfile_path)
table_sheetName = workbook.sheet_by_name('登陆页面业务组件')
logger = Logger(logger='HomePage').getlog()
class HomePage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)        # 继承父类，并调用父类的初始化方法
        self.input_username = table_sheetName.cell(1,1).value   # 读取excel表中用户名输入框元素
        self.input_password = table_sheetName.cell(2,1).value   # 读取excel表中密码输入元素
        self.rempwd = table_sheetName.cell(3,1).value           # 读取excel表中是否记住密码按钮元素
        self.loginBtn = table_sheetName.cell(4,1).value         # 读取excel表中登陆按钮元素
        self.centerBtn = table_sheetName.cell(6,1).value        # 读取excel表中切换到中心用户的按钮
        logger.info("读取excel文件中登陆页面相关元素数据完成")
    def center_user(self):
        self.click(self.centerBtn)
    def user(self,text):
        self.type(self.input_username,text)
    def pwd(self,text):
        self.type(self.input_password,text)
    def ifrempwd(self):
        self.click(self.rempwd)
    def login(self):
        self.click(self.loginBtn)