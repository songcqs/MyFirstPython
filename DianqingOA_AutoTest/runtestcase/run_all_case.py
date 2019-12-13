'''
  Code description： TestLoader测试case,并执行得到的所有测试集，生成html文件的测试报告并邮件发送测试报告
  Create time：2018-11-20
  Developer：
'''
# -*- coding: utf-8 -*-
import HTMLTestRunner  # 导入开源的测试报告生成HTML格式的模块
import os.path
import time
import unittest
import configparser  # 解析配置文件模块
from email.mime.text import MIMEText
from email.header import Header
import smtplib

"""
发邮件需要用到python两个模块，smtplib和email，这俩模块是python自带的，只需import即可使用。
smtplib模块主要负责发送邮件，email模块主要负责构造邮件。
其中MIMEText()定义邮件正文，Header()定义邮件标题。MIMEMulipart模块构造带附件
"""


# ===============定义邮件发送============
def send_mail(file_new):
    config = configparser.ConfigParser()
    file_path = os.path.dirname(os.path.abspath('.')) + '/V2200/config/config.ini'
    config.read(file_path, encoding='UTF-8')  # 读取config配置文件
    emailserver = config.get("emailserver", "emailservice")
    from_user = config.get("emailfrom_user", "from_user")
    from_passwd = config.get("emailfrom_passwd", "from_passwd")
    to_user = config.get("emailto", "to_user")

    f = open(file_new, 'rb')
    mail_boy = f.read()
    f.close()
    msg = MIMEText(mail_boy, 'html', 'utf-8')  # 定义邮件正文
    msg['Subject'] = Header('V2200自动化测试报告', 'utf-8')  # 定义邮件标题
    smtp = smtplib.SMTP()
    smtp.connect(emailserver)  # 连接邮箱服务器
    smtp.login(from_user, from_passwd)  # 邮件发送方登陆
    smtp.sendmail(from_user, to_user, msg.as_string())  # 邮件发送者和接收者
    smtp.quit()
    print("邮件已经发送，请注意查收！")


# ==============找到最新生成的测试报告文件===========
def new_report(report_path):
    lists = os.listdir(report_path)  # 得到项目目录下所有的文件和文件夹
    lists.sort(key=lambda fn: os.path.getmtime(report_path + '\\' + fn))  # 将得到的文件和文件夹按创建时间排序
    file_new = os.path.join(report_path, lists[-1])  # 获取最新创建的文件
    print(file_new)
    return file_new


# 测试用例路径
# case_path = os.path.join(os.getcwd(),'testcase')
case_path = os.path.abspath('E:\V2200_AutoTest\\testcase')
print(case_path)
# 测试报告路径
report_path = os.path.abspath('E:\V2200_AutoTest\\testreport')
print(report_path)


def all_case():
    '''
    找到case_path路径下所有以test_login开头的测试用例文件,保证每个子目录都是一个包文件，即该目录下
    有__init__.py文件，才能获取到多个目录下的所有test*.py的文件下的所有测试用例
    '''
    all_case = unittest.defaultTestLoader.discover(case_path, pattern="test_login*.py", top_level_dir=None)
    print(all_case)
    return all_case


if __name__ == '__main__':
    # 获取当前时间，并格式化时间
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # html测试报告路径
    report_html = os.path.join(report_path, "result_" + now_time + ".html")
    fp = open(report_html, 'wb')  # 打开一个文件，将测试结果写入该文件中
    '''
    wb:以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
    即原有内容会被删除。如果该文件不存在，创建新文件
    '''
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                            title=u'V2200自动化测试报告，测试结果如下：',
                                            description=u'用例执行情况：')

    runner.run(all_case())  # 执行所有测试case
    fp.close()
    mail_report = new_report(report_path)
    send_mail(mail_report)