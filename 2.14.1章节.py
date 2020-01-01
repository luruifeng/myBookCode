###2.14.1  自动化封装实战-第一部

from selenium import webdriver
from selenium.webdriver.common.by import By             #导入By类
from selenium.webdriver.support.ui import WebDriverWait   #导入WebDriverWait类
from selenium.webdriver.support import expected_conditions as EC  #导入EC模块
import time
def Element_Locator(*new_loctor):
    '''重写find_element定位方法'''
    return driver.find_element(*new_loctor)
def input_username(username,*userLoctor):
    '''输入用户名'''
    return Element_Locator(*userLoctor).send_keys(username)
def input_password(password,*passwdLoctor):
    '''输入密码'''
    return Element_Locator(*passwdLoctor).send_keys(password)
def click_btn(*clickLoctor):
    '''点击登录按钮'''
    return Element_Locator(*clickLoctor).click()
def assert_Login_text(*assertText):
'''获取登录成功后的验证信息'''
    return Element_Locator(*assertText).text

if __name__ == '__main__':
    #定位器
    user_loc = (By.ID, 'mobilePhone')
    passwd_loc = (By.ID, 'password')
    click_loc = (By.ID, 'loginBtn')
    successLogin_loc = (By.CSS_SELECTOR,'a.fc-blue.mr-5')
    driver = webdriver.Chrome()  # 获取驱动
    driver.get('https://www.gjfax.com/toLogin')  # 获取测试网址
    driver.maximize_window()  # 最大化窗口
    time.sleep(3)
    driver.refresh()
    input_username('18513600235',*user_loc)     #输入账号
    input_password('a123456',*passwd_loc)       #输入密码
    click_btn(*click_loc)                         #点击登录按钮
    time.sleep(3)
    # 断言
    if assert_Login_text(*successLogin_loc) == '安全退出':
        print('测试用例通过！')
    else:
        print('测试用例失败！')