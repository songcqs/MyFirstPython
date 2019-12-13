'''
  Code description：测试登陆  Create time：2018-11-20  Developer：
'''
# -*- coding: utf-8 -*-
import unittest
# unittest执行测试用例，默认是根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。
import time
from DianqingOA_AutoTest.DianqingOA.test.models.browser_engine import BrowserEngine
from DianqingOA_AutoTest.DianqingOA.test.page_obj.home_page import HomePage
import xlrd

excelfile_path = 'E:\V2200_AutoTest\V2200\data\\testdata\elementData.xlsx'
workbook = xlrd.open_workbook(excelfile_path)
table_sheetName = workbook.sheet_by_name('登陆页面业务组件')


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 测试前置条件
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # 测试结束后环境的复原
        cls.driver.quit()

    # case1:正确的用户密码登陆
    def test_1_login_sucess(self):
        homepage = HomePage(self.driver)
        homepage.user(table_sheetName.cell(1, 2).value)  # 读取excel中的数据
        homepage.pwd(table_sheetName.cell(2, 2).value)
        homepage.ifrempwd()
        homepage.login()
        time.sleep(2)
        try:
            assert '视频监控' in homepage.get_page_title()
            print('test title success')
            homepage.get_window_img()  # 调用Basepage类封装的截图方法
        except Exception as e:
            print('test title error', format(e))


if __name__ == '__main__':
    unittest.main()  # 将一个单元测试模块变成可以直接运行的测试脚本