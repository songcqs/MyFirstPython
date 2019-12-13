'''
  Code description：封装浏览器引擎类，读取配置文件实现浏览器类型的选择，并封装打开浏览器和退出的方法
  Create time：2018-11-12
  Developer：
'''
# -*- coding: utf-8 -*-
import configparser  # python解析配置文件模块
import os.path
from selenium import webdriver
from DianqingOA_AutoTest.DianqingOA.test.models.log import Logger # 引入日志类模块

logger = Logger(logger="BrowserEngine").getlog()  # 实例化对象logger

class BrowserEngine(object):
    def __init__(self, driver):
        self.driver = driver  # 初始化构造函数，将参数driver self化便于后面创建的方法直接自动调用

    def open_browser(self, driver):
        '''
        :param driver: 读取配置文件，返回driver
        :return:
        '''
        config = configparser.ConfigParser() # 实例化configParser对象
        file_path = os.path.abspath(r'D:\python-workspace\我的python程序\DianqingOA_AutoTest\DianqingOA\config\config.ini')  # 绝对路径写法
        # print('得到的读取config文件的路径：',file_path)
        config.read(file_path, encoding='UTF-8')  # 读取配置文件

        browser = config.get("browserType", "browserName")
        logger.info("选择的浏览器是： %s ." % browser)
        url = config.get("testServer", "URL")
        logger.info("测试的平台URL是: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.get(url)  # 得到测试的url
        logger.info("浏览器的版本为：%s" % driver.capabilities['version'])  # 获取浏览器版本

        driver.maximize_window()
        logger.info("最大化浏览器窗口.")

        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        self.driver.quit()