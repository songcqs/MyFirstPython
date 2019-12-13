import unittest

class MyTest(unittest.TestCase):    # 继承unittest.TestCase
    def setUp(self):
        print("setUp每个测试用例执行之前做操作")
    def tearDown(self):
        print("tearDown每个测试用例执行之后做操作")

    @classmethod
    def setUpClass(cls):
        print("setUpClass必须使用@classmethod 装饰器,所有test运行前运行一次")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass必须使用 @ classmethod装饰器, 所有test运行完后运行一次")

    def test_a_run(self):
        self.assertEqual(1,1)

    def test_b_run(self):
        self.assertNotEqual(1, 2)

'''
        assertEqual(a, b)     a == b      
        assertNotEqual(a, b)     a != b      
        assertTrue(x)     bool(x) is True      
        assertFalse(x)     bool(x) is False      
        assertIsNone(x)     x is None     
        assertIsNotNone(x)     x is not None   
        assertIn(a, b)     a in b    
        assertNotIn(a, b)     a not in b
'''

if __name__ == '__main__':
    unittest.main() #运行所有的测试用例


def myrange(times):
    for i in range(times):
        print("i----------:",i)

myrange(4)

>> >
>> > mo = re.compile(r'(?<=SRC=)"([\w+\.]+)"', re.I)

>> > mo.sub(r'"\1****"', line)
'<IMG ALIGN="middle" SRC=\'#\'" /span>

>> > mo.sub(r'replace_str_\1', line)
'<IMG ALIGN="middle" replace_str_overview.gif BORDER="0" ALT="">' < / span >

>> > mo.sub(r'"testetstset"', line)
'<IMG ALIGN="middle" SRC=\'#\'" /span>

