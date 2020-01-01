####2.12.6  Parameterized参数化实战
import unittest
from selenium import webdriver
from time import sleep
from parameterized import parameterized  #导入参数化模块
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.testUrl = 'https://mail.sohu.com/fe/#/login'
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def by_css(self, usernameloc):
        '''重写css定位'''
        return self.driver.find_element_by_css_selector(usernameloc)
    def getassertText(self):
        '''获取验证信息'''
        try:
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位报错!报错原因是：{}'.format(message))
    def souhuLogin(self, user, passwd):
        '''封装登录功能'''
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
        self.by_css('.btn-login.fontFamily').click()
上述代码，对搜狐邮箱登录、css元素定位、登录后的验证信息功能进行二次封装。封装后的方法分别是souhuLogin()、by_css()、getassertText()。
@parameterized.expand([
        ('', '', '请输入账号密码'),
        ('admin111@sohu.com', '', '请输入账号密码'),
('', 'a123456789', '请输入账号密码')])
    def test_login(self,username, password, assert_text):
        #登录系统
        self.driver.get(self.testUrl)
        sleep(3)
        self.souhuLogin(username,password)
        self.assertEqual(self.getassertText(), assert_text)
if __name__ == '__main__':
    unittest.main(verbosity=2)