import os,time,unittest
from HTMLTestRunner import HTMLTestRunner
def getAllCases():
   '''获取tesTcase下面的所有测试模块'''
   Testsuite = unittest.defaultTestLoader.discover(
      start_dir=os.path.join(os.path.dirname(__file__),'TestCases'),
      pattern='test*.py')
   return Testsuite
def RunMain():
'''生成测试报告写入指定Reports目录'''
   fp=open(os.path.join(os.path.dirname(__file__),'Reports',
time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
   HTMLTestRunner(stream=fp,title='Python+Selenium自动化测试实战',
                   description='基于python语言UI自动化测试').run(getAllCases())
if __name__ == '__main__':
   RunMain()