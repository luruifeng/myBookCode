###2.12.3  Excel自动化测试实战

import xlrd
import ddt,unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   #导入WebDriverWait类
from selenium.webdriver.support import expected_conditions as EC  # 导入EC模块
def readUserName(row):
    '''读取用户名'''
    book  = xlrd.open_workbook('datainfo.xlsx','r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[0]
def readPasswd(row):
    '''读取用户名'''
    book  = xlrd.open_workbook('datainfo.xlsx','r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[1]
def readAssertText(row):
    '''读取预期结果'''
    book  = xlrd.open_workbook('datainfo.xlsx','r')
    table = book.sheet_by_index(0)
    return table.row_values(row)[2]



 class TestSouHuLogin(unittest.TestCase):
    def  setUp(self):
        self.driver = webdriver.Chrome()
        self.testUrl = "https://mail.sohu.com/fe/#/login"
    def  tearDown(self):
        self.driver.quit()
    def  by_css(self,usernameloc):
        '''重写css定位'''
        return self.driver.find_element_by_css_selector(usernameloc)
    def  getassertText(self):
        '''获取验证信息'''
        try:
            sleep(2)
            loctor = (By.CSS_SELECTOR,'.tipHolder.ng-binding')
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位报错!报错原因是：{}'.format(message))
    def  souhuLogin(self,user,passwd):
        '''封装登录功能'''
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(passwd)
        self.by_css('.btn-login.fontFamily').click()
    def  test_souHuLogin_001(self):
        '''账号和密码为空：登录失败'''
        self.driver.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readUserName(1),readPasswd(1))
        self.assertEqual(self.getassertText(), readAssertText(1))
    def  test_souHuLogin_002(self):
        '''账号正确和密码为空：登录失败'''
        self.driver.get(self.testUrl)
        self.souhuLogin(readUserName(2), readPasswd(2))
        self.assertEqual(self.getassertText(), readAssertText(2))
    def  test_souHuLogin_003(self):
        '''账号错误和密码为空：登录失败'''
        self.driver.get(self.testUrl)
        self.souhuLogin(readUserName(3), readPasswd(3))
        self.assertEqual(self.getassertText(), readAssertText(3))
    def  test_souHuLogin_004(self):
        '''账号为空和密码正确：登录失败'''
        self.driver.get(self.testUrl)
        self.souhuLogin(readUserName(4), readPasswd(4))
        self.assertEqual(self.getassertText(), readAssertText(4))
if __name__ == '__main__':
    unittest.main()