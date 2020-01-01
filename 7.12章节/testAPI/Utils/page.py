#coding=utf-8
#@time   :2019/1/1 13:33
#@Author :Keep Learing
#@boke   :www.cnblogs.com/fighter007
#@motto  :Keep Learing

import logging
import os,requests
import configparser #导入configparser模块

class Helper(object):

    def dirname(self,fileName='',filepath='Data'):
        '''
        :param fileName: 文件名字
        :param filepath: 写入指定目录
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,fileName)

    def get(self,url,headers=''):
        '''重构GET请求'''
        if url:
            r = requests.get(url=url,headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as M:
                print('错误原因：%s'%M)

    def post(self,url,data,headers=''):
        '''重构POST请求'''
        if url:
            r = requests.post(url=url,json=data,headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as M:
                print('错误原因：%s'%M)

    def delete(self,url,headers=''):
        '''重构DELETE请求'''
        if url:
            r = requests.delete(url=url,headers=headers)
            return r
        else:
            try:
                print('接口地址有误！')
            except Exception as M:
                print('错误原因：%s'%M)

    def Makelog(self,log_content):
       '''定义log日志级别'''
       #定义日志文件
       logFile = logging.FileHandler(self.dirname('log.txt','Log'), 'a',encoding='utf-8')
       # 设置log格式
       fmt=logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
       logFile.setFormatter(fmt)
       logger1 = logging.Logger('logTest',level=logging.DEBUG)   #定义日志
       logger1.addHandler(logFile)
       logger1.info(log_content)
       logFile.close()

    def readConfig(self):
        '''读取配置文件中的内容'''
        l = []
        config = configparser.ConfigParser()
        config.read(self.dirname('config.ini','Config'),encoding='utf-8')
        email_host = config.get("EMAIL","mail_host")
        email_password = config.get("EMAIL","mail_pass")
        email_sender = config.get('EMAIL','sender')
        email_user = config.get('EMAIL','mail_user')
        email_receiver = config.get('EMAIL','receiver')
        email_subject = config.get('EMAIL','subject')
        l.append(email_host)
        l.append(email_password)
        l.append(email_sender)
        l.append(email_user)
        l.append(email_receiver)
        l.append(email_subject)
        return  l

p = Helper()
print(p.readConfig())
# print(per.dirname('token'))











