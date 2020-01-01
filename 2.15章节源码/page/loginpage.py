#-*- coding=utf-8 -*-
__author__ = 'Fighter.Lu'

import sys
sys.path.append('../basePage')
from homePage import HomePage   #导入基础类
from selenium.webdriver.common.by import By #定位方式
from time import sleep


#登录的页面类
class LoginPage(HomePage):
	#定位器
	#用户名
	username_loc = (By.ID,'mobilePhone')
	#密码
	password_loc = (By.ID,'password')
	#登录按钮
	loginBtn_loc = (By.ID,'loginBtn')
	#退出连接
	logoutBtn_loc = (By.CSS_SELECTOR,'a.fc-blue.mr-5')
	#用户名为空
	userNull_loc = (By.CSS_SELECTOR,'#error > span.error')
	#密码为空
	passWordNull_loc = (By.CSS_SELECTOR,'#error > span.error')

	#打开登陆页面
	def openLoginPage(self):
		self.dr.get(self.url)
		self.dr.refresh()
		self.dr.maximize_window()
		sleep(0.5)

	#输入用户名
	def input_userName(self,userName):
		self.find_element(*self.username_loc).send_keys(userName)

	#输入密码
	def input_passWord(self,password):
		self.find_element(*self.password_loc).send_keys(password)

	#点击登录按钮
	def click_loginBtn(self):
		self.find_element(*self.loginBtn_loc).click()

	#获取登录成功后的提示信息
	def get_assertText(self):
		sleep(3)
		return self.find_element(*self.logoutBtn_loc).text

	#用户名为空的提示
	def get_userNullText(self):
		return self.find_element(*self.userNull_loc).text

	#密码为空的提示
	def get_passwordNullText(self):
		return self.find_element(*self.passWordNull_loc).text

	#组装成登录流程
	def login_gjs_pro(self,username,password):
		self.input_userName(username)
		self.input_passWord(password)
		self.click_loginBtn()



