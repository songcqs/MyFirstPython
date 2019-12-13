import unittest
import xmlrunner
# Jenkins认识xml格式的报告，产生xml格式的，就需要用一个新的模块 xmlrunner，安装直接 pip install xmlrunner即可

# 导入这个模块
class My(unittest.TestCase):
    def test1(self, a, b, c):
        self.assertEqual(a + b, c)


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(My))
    runner = xmlrunner.XMLTestRunner(output='report')  # 指定报告放的目录
    runner.run(test_suite)