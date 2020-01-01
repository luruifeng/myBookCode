#-*- coding=utf-8 -*-
__author__ = 'Fighter.Lu'

import sys,unittest
sys.path.append('../common')
sys.path.append('../page')
from ownUnit import MyunitTests  #导入测试关键所在类
from helper import Helper        #新增Helper类
from time import sleep

from getImage import SaveImage  #导入截图功能
import logging  #导入日志模块


class TestLogin(MyunitTests,Helper):

	# def  test_login(self):
	# 	'''正确的用户名和密码'''
	# 	self.loginpage.openLoginPage()
	# 	self.log('PO-gjs：打开浏览器进入到项目首页')
	# 	self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
	# 	self.log('PO-gjs：输入正确的用户名和密码')
	# 	sleep(5)
	# 	self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))  #断言
	# 	self.log('PO-gjs：登录成功获取信息进行断言')
	# 	SaveImage(self.dr,'login_success.png')
	# 	self.log('PO-gjs：登录成功后获取截图信息')
	# 	self.log('PO-gjs：第4条用例执行结束.....')


	def test_user_null(self):
		'''测试密码为空'''
		self.loginpage.openLoginPage()
		self.log('PO-gjs：打开浏览器进入到项目首页')
		self.loginpage.login_gjs_pro(self.readusername(2),self.readpassword(2))
		self.log('PO-gjs：输入正确用户名和密码为空')
		self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(2))  #断言
		self.log('PO-gjs：登录失败获取信息进行断言')
		SaveImage(self.dr,'loginpasswdNull.png')
		self.log('PO-gjs：登录失败后获取截图信息')
		self.log('PO-gjs：第1条用例执行结束.....')

	def test_username_null(self):
		'''测试用户名为空'''
		self.loginpage.openLoginPage()
		self.log('PO-gjs：打开浏览器进入到项目首页')
		self.loginpage.login_gjs_pro(self.readusername(3),self.readpassword(3))
		self.log('PO-gjs：输入用户名为空和正确密码')
		self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(3))
		self.log('PO-gjs：登录失败获取信息进行断言')
		SaveImage(self.dr,'loginuserNull.png')
		self.log('PO-gjs：登录失败后获取截图信息')
		self.log('PO-gjs：第3条用例执行结束.....')


	def test_user_passwd_null(self):
		'''测试用户名/密码为空'''
		self.loginpage.openLoginPage()
		self.log('PO-gjs：打开浏览器进入到项目首页')
		self.loginpage.login_gjs_pro(self.readusername(4),self.readpassword(4))
		self.log('PO-gjs：输入用户名为空和正确为空')
		self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(4))
		self.log('PO-gjs：登录失败获取信息进行断言')
		SaveImage(self.dr,'loginuserAndpasswd.png')
		self.log('PO-gjs：登录失败后获取截图信息')
		self.log('PO-gjs：第2条用例执行结束.....')


if __name__ == '__main__':
    unittest.main(verbosity=2)




# self.loginpage.openLoginPage()
# self.log('测试正常的登录：po自动化测试-->打开登录页面')
# # 输入账号
# self.loginpage.input_userName(self.readusername(1))
# self.log('测试正常的登录：po自动化测试-->输入账号')
# # 输入密码
# self.loginpage.input_passWord(self.readpassword(1))
# self.log('测试正常的登录：po自动化测试-->输入密码')
# # 点击登录
# self.loginpage.click_loginBtn()
# self.log('测试正常的登录：po自动化测试-->点击登录按钮')
# # 断言
# self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
# self.log('测试正常的登录：po自动化测试-->验证登录是否成功！')


# import xlrd,logging
# from PO.common.helper import *           ,Helper  继承

	# #测试密码为空
	# def test_user_null(self):
	# 	#打开登录页面
	# 	self.loginpage.openLoginPage()
	# 	self.log('测试密码为空：po自动化测试-->打开登录页面')
	# 	#输入账号
	# 	self.loginpage.input_userName(self.readusername(2))
	# 	self.log('测试密码为空：po自动化测试-->输入账号')
	# 	#输入密码
	# 	self.loginpage.input_passWord(self.readpassword(2))
	# 	self.log('测试密码为空：po自动化测试-->输入密码')
	# 	#点击登录
	# 	self.loginpage.click_loginBtn()
	# 	self.log('测试密码为空：po自动化测试-->点击登录按钮')
	# 	#断言
	# 	self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(2))
	# 	self.log('测试密码为空：po自动化测试-->验证登录是否成功！')
    #
	# #测试用户名为空
	# def test_password_null(self):
	# 	#打开登录页面
	# 	self.loginpage.openLoginPage()
	# 	#输入账号
	# 	self.loginpage.input_userName(self.readusername(3))
	# 	#输入密码
	# 	self.loginpage.input_passWord(self.readpassword(3))
	# 	#点击登录
	# 	self.loginpage.click_loginBtn()
	# 	#断言
	# 	self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(3))





