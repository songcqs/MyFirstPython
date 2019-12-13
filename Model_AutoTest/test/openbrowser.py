# coding = utf-8
from selenium import webdriver
import time

"""打开IE浏览器"""
'''方式一：直接打开IE浏览器'''
# driver = webdriver.Ie()                                                  # 可直接启动IE

'''方式二：配置IE的path与option打开IE浏览器'''
# IE定义path
# path = "D:\\Python37\\IEDriverServer.exe"                                   # OK成功，可启动IE
# path或=
# path = "C:\\Program Files\\Internet Explorer\\IEDriverServer.exe"           # OK成功，可启动IE
# path或=
# path = "D:\\python-workspace\\我的第一个python程序\\IEDriverServer.exe"     # OK成功，可启动IE

# IE定义option
# option = webdriver.IeOptions()
#
# 创建新的IE会话
# driver = webdriver.Ie(executable_path=path,ie_options=option)

"""打开Firefox浏览器"""
'''方式一：直接打开Firefox浏览器'''
# driver = webdriver.Firefox()                                               #启动成功，但没有主页

'''方式二：配置Firefox的path与option打开Firefox浏览器'''
# Firefox定义path
# path = "D:\\Python37\\geckodriver.exe"                                       #启动成功，但没有主页
# path = "D:\\Program Files (x86)\\Mozilla Firefox\\geckodriver.exe"            #启动成功，但没有主页
# path = "D:\\python-workspace\\我的第一个python程序\\geckodriver.exe"          #启动成功，但没有主页
# path = "D:\\Program Files (x86)\\Mozilla Firefox\\geckodriver.exe"         #启动成功，但没有主页
# path = "D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"             #启动成功，但未进入百度页面

# Firefox定义option
# option = webdriver.FirefoxOptions()

# 创建新的Firefox会话
# driver = webdriver.Firefox(executable_path=path,firefox_options=option)

"""打开Chrome浏览器"""
'''方式一：直接打开Chrome浏览器'''
driver = webdriver.Chrome()                                                   # 启动成功

'''方式二：配置Chrome的path与option打开Chrome浏览器'''
# Chrome定义path
# path = "D:\\Python37\\chromedriver.exe"                                         # 启动成功
# path = "D:\\python-workspace\\我的第一个python程序\\chromedriver.exe"             # 启动成功
# path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"            # 启动成功
# path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 启动成功

# Chrome定义option
# option = webdriver.ChromeOptions()

# 创建新的Chrome会话
# driver = webdriver.Chrome(executable_path=path, chrome_options=option)

driver.get("http://www.baidu.com")  # 通过get()方法，打开一个url站点
print(driver.title)
time.sleep(1)
driver.maximize_window()  # 最大化浏览器
driver.quit()  # 关闭并退出浏览器

