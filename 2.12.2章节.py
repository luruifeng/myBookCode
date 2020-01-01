
##2.12.2  DDT在自动化测试中的应用

import ddt
import unittest
Data = [{'name':"keep learing"},
        {'age':18},
        {'address':"深圳地区"}]
@ddt.ddt
class TestModules(unittest.TestCase):
    def setUp(self):
        print('testcase beaning....')
    def tearDown(self):
        print('testcase ending.....')
    @ddt.data(*Data)
    def test_DataDriver(self,Data):
        print('DDT数据驱动实战演示：',Data)
if __name__ == '__main__':
    unittest.main()