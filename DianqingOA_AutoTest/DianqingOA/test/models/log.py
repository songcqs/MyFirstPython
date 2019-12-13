'''
  Code description：封装日志类，定义日志文件输出格式和日志输出级别
  Create time：2018-11-8
  Developer：
'''
# -*- coding: utf-8 -*-
import logging
import time
import os.path


class Logger(object):
    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        self.logger = logging.getLogger(logger)

        # 设置日志默认级别为DEBUG
        self.logger.setLevel(logging.DEBUG)

        # 设置日志输出格式
        fmt = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')

        # 格式化当前时间
        currTime = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

        # 设置日志文件保存路径
        log_path = os.path.dirname(os.path.abspath('D:\\python-workspace\\我的python程序\\DianqingOA_AutoTest\\testcase')) + '/log/logs/'
        # log_path = os.path.dirname(os.path.abspath('.')) + '/log/logs/'      # 相对路径写法
        # print(os.path.dirname(os.path.abspath('E:\V2200_AutoTest\\testcase')))
        print('得到的日志路径为：', log_path)

        # 设置日志文件名称
        log_name = log_path + currTime + '.log'

        # 设置由文件输出
        fh = logging.FileHandler(log_name, encoding='utf-8')  # 采用utf-8字符集格式防止出现中文乱码
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)  # 日志级别为INFO

        # 设置日志由控制台输出
        # sh = logging.StreamHandler(log_name)
        # sh.setFormatter(fmt)
        # sh.setLevel(CmdLevel)
        self.logger.addHandler(fh)  # 添加handler

    def getlog(self):
        return self.logger