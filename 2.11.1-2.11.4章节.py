##2.11.1  unittest简介
import unittest
class TestStrSample(unittest.TestCase):
    def test_strendswich(self):
        self.assertEqual('foo'.endswith('o'),False)
    def test_split(self):
        s = 'my name is Fighter'
        self.assertEqual(s.split(), ['my', 'name','is','Fighter'])
if __name__ == '__main__':
    unittest.main()

##2.11.2  前置和后置
import unittest
class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('每条测试用例开始执行前做的操作.....')
    def test_isupper(self):
        self.assertTrue('FOO'.endswith('O'))
        self.assertFalse('Foo'.isupper())
        print('第一条测试用例')
    def test_strendswich(self):
        self.assertEqual('foo'.endswith('o'), True)
        print('第二条测试用例')
    def tearDown(self):
        print('每条测试用例执行完毕后做的操作.....')
if __name__ == '__main__':
    unittest.main()



##2.11.3  常用断言方法
import unittest
from selenium import webdriver
from time import sleep
class TestWebUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
    def test_QQLogin(self):
        self.driver.get('https://mail.qq.com/cgi-bin/loginpage')
        self.assertEqual(self.driver.title,'登录QQ邮箱',’页面跳转失败，请重新检查！’)
    def test_MaoyanMovie(self):
        self.driver.get('https://maoyan.com/')
        self.assertEqual(self.driver.title,'猫眼电影 - 一网打尽好电影',’页面跳转失败,请重新检查！’)
if __name__ == '__main__':
    unittest.main()


##2.11.4  setUpClass和tearDownClass
import unittest
from selenium import webdriver
from time import sleep
class TestWebUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_QQLogin(self):
        self.driver.get('https://mail.qq.com/cgi-bin/loginpage')
        self.assertEqual(self.driver.title,'登录QQ邮箱')
    def test_MaoyanMovie(self):
        self.driver.get('https://maoyan.com/')
        self.assertEqual(self.driver.title,'猫眼电影 - 一网打尽好电影')
if __name__ == '__main__':
    unittest.main()