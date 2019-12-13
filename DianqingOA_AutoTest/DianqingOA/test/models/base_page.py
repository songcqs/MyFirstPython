'''
  Code description：页面基类，封装所有页面共用的方法
  Create time：2018-11-13
  Developer：
'''
# -*- coding: utf-8 -*-
import time
import os.path
from DianqingOA_AutoTest.DianqingOA.test.models.log import Logger
from selenium.common.exceptions import NoSuchElementException  # selenium下封装的判断元素是否存在的模块

logger = Logger(logger='BasePage').getlog()

class BasePage(object):
    # 构造方法,初始化参数driver,用于后面的方法直接调用
    def __init__(self, driver):
        self.driver = driver

    # 浏览器前进
    def forward_browser(self):
        self.driver.forward()
        logger.info("在当前页面中点击浏览器前进.")

    # 浏览器后退
    def back_browser(self):
        self.driver.back()
        logger.info("在当前页面中点击浏览器后退.")

    # 设置隐式等待时间
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("设置隐式时间：%d 秒." % seconds)

    # 关闭当前窗口
    def close_window(self):
        try:
            self.driver.close()
            logger.info("关闭当前窗口.")
        except NameError as e:
            logger.error("关闭当前窗口出错，抛出错误提示：%s." % e)

    # 截图功能:得到截图并保存图片到项目image目录下
    def get_window_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/image/'  # 设置存放截图的路径
        # print('截图保存路径为：%s' % file_path)
        timeset = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 格式化时间
        pic_name = file_path + timeset + '.png'  # 定义截图文件名称
        try:
            self.driver.get_screenshot_as_file(pic_name)
            logger.info('截图成功，图片保存路径为：/image.')
        except Exception as e:
            logger.error('截图出现异常', format(e))
            self.get_window_img()

    # 8大页面元素（对象）定位方法的封装
    def find_element(self, selector):
        '''
        使用‘=>’作为字符串分割符，后续实际测试用例根据输入的元素selector_by和selector_value 进行选择元素的定位类型
        :param selector:
        :return: element
        '''
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]  # 按=>分割符进行切割字符串，返回一个列表，得到列表的第一个元素，即元素的定位方法
        selector_value = selector.split('=>')[1]  # 得到列表的第二个元素，即元素定位的值

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("定位元素OK，实际定位元素方法：%s ,定位的元素的属性值：%s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没找到元素，抛出异常：%s" % e)
                self.get_window_img()  # 截取当前窗口
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("定位元素OK，实际定位元素方法：%s ,定位的元素的属性值：%s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没找到元素，抛出异常：%s" % e)
                self.get_window_img()  # 截取当前窗口
        elif selector_by == 'c' or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("请输入正确的目标元素类型.")
        return element  # 返回变量element

    # 封装输入框方法
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入的文本内容为：%s" % text)
        except NameError as e:
            logger.error("输入的内容异常，抛出异常：%s" % e)
            self.get_window_img()

    # 清除文本内容
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("清除输入框文本信息OK")
        except NameError as e:
            logger.error("清除输入框内容失败：抛出异常: %s" % e)
            self.get_window_img()

    # 封装点击元素的动作
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("点击元素动作完成")
        except NameError as e:
            logger.error("点击事件失败，抛出异常：%s" % e)

    # 获取打开的url地址标题
    def get_page_title(self):
        logger.info("当前打开的url地址标题为：%s" % self.driver.title)
        return self.driver.title

    # 获取警示框，并得到提示框信息和关闭提示框
    def get_alert(self):
        el = self.driver.switch_to.alert  # 获取窗口弹窗的方法
        try:
            assert '用户名或者密码错误' in el.text  # el.text方法获取提示框内容
            logger.info("弹窗提示正确")
            el.accept()  # 点击弹窗确认按钮
        except Exception as e:
            print('弹窗提示错误', format(e))

    @staticmethod  # 静态方法：不强制要求传递参数，类可以不用实例化就能调用该方法
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("等待时间是：%s 秒" % seconds)