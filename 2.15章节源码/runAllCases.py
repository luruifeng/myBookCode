#-*- coding=utf-8 -*-
__author__ = 'Fighter.Lu'


import sys,os,time,unittest
sys.path.append('./common')
sys.path.append('./basepage')
sys.path.append('./page')
from HTMLTestRunner import HTMLTestRunner

def getAllCases():
	'''获取tesTcase下面的所有测试模块'''
	Testsuite = unittest.defaultTestLoader.discover(
		start_dir=os.path.join(os.path.dirname(__file__),'TestCases'),
		pattern='test*.py')
	return Testsuite

def RunMain():
	'''生成测试报告写入指定Reports目录'''
	fp=open(os.path.join(os.path.dirname(__file__),'report',time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
	HTMLTestRunner(stream=fp,title='Python+Selenium自动化测试实战',
				   description='基于python语言PO自动化测试').run(getAllCases())

if __name__ == '__main__':
   RunMain()

















# import  unittest,os,time
# from PO.common.HTMLTestRunner import HTMLTestRunner
#
# def  allTest():
# 	'''获取testCases下面的所有测试用例'''
# 	case = os.path.join(os.path.dirname(__file__),'TestCases')
# 	suite = unittest.defaultTestLoader.discover(case,pattern='test*.py')
# 	return suite
#
# def getTime():
# 	'''获取当前系统时间'''
# 	return time.strftime("%Y_%m_%d_%H_%M_%S")
#
# def run():
# 	'''主函数入口'''
# 	report = os.path.join(os.path.dirname(__file__),'report',getTime())  +  '_report.html'
# 	HTMLTestRunner(stream=open(report,'wb'),title='po自动化测试设计模式',description='window10 chrome67').run(allTest())
#
#
# if __name__ == '__main__':
#     run()