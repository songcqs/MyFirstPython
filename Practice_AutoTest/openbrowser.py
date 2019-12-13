# coding=utf-8
print("Hello,nice to meet you!")

from selenium import webdriver                                # 导入webdriver包

# profileDir = "D:/Program Files (x86)/Mozilla Firefox/"      # 给出本地的配置地址
# profile = webdriver.FirefoxProfile(profileDir)              # 读取本地配置
# driver = webdriver.Firefox()                                # 打开本地火狐

# profileDir = "C:/Program Files (x86)/Google/Chrome/Application/"  #给出chromedriver的路径
# proile = webdriver.ChromeOptions(profileDir)
# driver = webdriver.Chrome()                                       #打开本地谷歌

# driver = webdriver.Firefox()                                 # 初始化一个火狐浏览器实例：driver
# driver = webdriver.Chrome()                                  # 调用谷歌浏览器
# driver = webdriver.Ie()                                      # 调用IE浏览器

options = webdriver.ChromeOptions()                        # 调用ChromeOptions方法

options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "/usr/bin/chromedriver"
# chrome_driver_binary = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
options = webdriver.ChromeOptions()  #调用ChromeOptions方法
driver = webdriver.Chrome(chrome_driver_binary,chrome_options = options)

#初始化，通过selenium打开chrome浏览器
driver.get("https://www.baidu.com")  # 通过get()方法，打开一个url站点

driver.maximize_window()  # 最大化浏览器
driver.quit()  # 关闭并退出浏览器