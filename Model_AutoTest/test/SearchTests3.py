import unittest
from selenium import webdriver

"""setUpClass(),tearDownClass()方法,@classmethod标识,在类级别来初始化数据,让各个测试方法共用一个Firefox实例"""
class SearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com/")
        cls.driver.title

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2, len(products))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()

        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
        
    if __name__ == '__main__':
            unittest.main()

