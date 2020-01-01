####2.12.5  YAML自动化测试实战
import unittest,yaml
from time import sleep
from selenium import webdriver
def readYaml():
   '''获取所有yaml所有数据'''
   f = open('data.yaml', 'r', encoding='utf-8')
   data = yaml.load(f)
   f.close()
   return data
class TestLogin(unittest.TestCase):
   def setUp(self):
      self.driver = webdriver.Chrome()
      self.testUrl = "https://mail.sohu.com/fe/#/login"
   def tearDown(self):
      self.driver.quit()
   def by_css(self,usernameloc):
      '''重写css定位'''
      return self.driver.find_element_by_css_selector(usernameloc)
   def getassertText(self):
      '''获取验证信息'''
      try:
         return self.by_css('.tipHolder.ng-binding').text
      except Exception as message:
         print('元素定位报错!报错原因是：{}'.format(message))
   def souhuLogin(self,user,passwd):
      '''封装登录功能'''
      self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
      self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
      self.by_css('.btn-login.fontFamily').click()
   def test_souHuLogin_001(self):
      '''账号正确和密码为空：登录失败'''
      self.driver.get(self.testUrl)
      sleep(3)
      self.souhuLogin(readYaml()['userNull']['username'],readYaml()['userNull']['password'])
      self.assertEqual(self.getassertText(), readYaml()['userNull']['assertText'])
   def test_souHuLogin_002(self):
      '''账号错误和密码为空：登录失败'''
      self.driver.get(self.testUrl)
      sleep(3)
      self.souhuLogin(readYaml()['passNull']['username1'],readYaml()['passNull']['password1'])
      self.assertEqual(self.getassertText(), readYaml()['passNull']['assertText1'])
if __name__ == '__main__':
   unittest.main()