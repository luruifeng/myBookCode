###2.14.2  自动化封装实战-第二部


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  #二次定位的By类
class GJsProject(object):
   def __init__(self):
      self.driver = webdriver.Chrome()   #定义驱动
   def openbrowser(self,url):            #定义基础操作
      self.driver.get(url)
      self.driver.maximize_window()
      sleep(2)
   def by_css(self,loc):
      '''重写css定位'''
      return self.driver.find_element(By.CSS_SELECTOR,loc)
   def click_login_btn(self,loc):             #点击登录按钮
      self.by_css(loc).click()
   def input_username_Text(self,loc,text):  #输入账号
      self.by_css(loc).send_keys(text)
   def input_password_Text(self,loc,text):  #输入密码
      self.by_css(loc).send_keys(text)
   def click_login_button(self,loc):        #点击登录按钮
      self.by_css(loc).click()
   def assert_success_text(self,loc):     #获取验证信息
      return self.by_css(loc).text    
   def logsys_gjs_action(self,loc):       #退出系统
      self.by_css(loc).click()
      sleep(2)
      self.driver.quit()


# 登录流程
   def login_gjs(self,url,loc1,loc2,username,loc3,password,loc4,loc5,exceptText,loc6):
      self.openbrowser(url)
      sleep(1)
      self.click_login_btn(loc1)
      sleep(1)
      self.input_username_Text(loc2,username)
      sleep(1)
      self.input_password_Text(loc3,password)
      sleep(1)
      self.click_login_button(loc4)
      sleep(1)
      if self.assert_success_text(loc5) == exceptText:  #断言登录是否成功
         print('pass')
      else:
         print('fail')
      self.logsys_gjs_action(loc6)

if __name__ == '__main__':
   t = GJsProject()
   url = 'https://www.gjfax.com/'           #打开项目地址
   loc1 = "span.menubar-btn .fc-white"    #定位器
   loc2 = "#mobilePhone"
   username = '18513600235'
   loc3 = "#password"
   password = 'a123456'
   loc4 = "#loginBtn"
   loc5 = "a.fc-blue.mr-5" 
   exceptText = '安全退出'
   loc6 = "a.fc-blue.mr-5"
   t.login_gjs(url,loc1,loc2,username,loc3,password,loc4,loc5,exceptText,loc6)  #调用登录方法