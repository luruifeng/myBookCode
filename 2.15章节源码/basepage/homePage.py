#-*- coding=utf-8 -*-
__author__ = 'Fighter.Lu'


from selenium.webdriver.support.wait import WebDriverWait   #显示等待
from selenium.webdriver.support import expected_conditions as EC  #判断元素是否被定位到


#页面的基础类
class HomePage():
	#构造方法
	def __init__(self,url,dr):
		self.url = url
		self.dr = dr

	#封装元素定位方式
	def find_element(self,*loc):
		try:
			WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(loc))
			return self.dr.find_element(*loc)
		except Exception as message:
			print('元素定位在页面中无法找到！{}'.format(message))
