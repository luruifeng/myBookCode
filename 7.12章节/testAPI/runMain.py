#coding=utf-8
#@time   :2018/12/27 22:10
#@Author :Keep Learing
#@boke   :www.cnblogs.com/fighter007
#@motto  :Keep Learing

import smtplib  #邮箱服务器
from email.mime.text import MIMEText  #邮件模版类
import unittest
from testAPI.Config.HTMLTestRunner import HTMLTestRunner
import time,os
from email.mime.multipart import MIMEMultipart #邮件附件类
from email.header import Header  #邮件头部模版
import configparser  #导入configparser模块
from testAPI.Utils.page import *


#发送带邮件的函数 动作
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    #基本信息
    smtpserver = Helper().readConfig()[0]
    pwd = Helper().readConfig()[1] #126邮箱授权码

    #定义邮件主题
    msg=MIMEMultipart()
    msg['subject'] = Header(Helper().readConfig()[-1],'utf-8')
    msg['from'] = Helper().readConfig()[2]   #必须加 不加报错  发送者的邮箱
    msg['to'] =  Helper().readConfig()[3]     #必须加 不加报错  接收者的邮箱

    #不加msg['to'] msg['from']报错原因，是因为“发件人和收件人参数没有进行定义

    #HTML邮件正文 直接发送附件的代码片段
    body=MIMEText(mail_body,"html","utf-8")
    msg.attach(body)
    att = MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="Interface_report.html"'
    msg.attach(att)

    #链接邮箱服务器发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(msg['from'],pwd)
    smtp.sendmail(msg['from'],msg['to'],msg.as_string())
    print ("邮件发送成功")


#查找最新邮件
def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)  #print(lists)  #列出测试报告目录下面所有的文件
    lists.sort()   #从小到大排序 文件
    file = [x for x in lists if x.endswith('.html')]  #for循环遍历以.html格式的测试报告
    file_path = os.path.join(result_dir,file[-1])  #找到测试报告目录下面最新的测试报告
    return file_path  #返回最新的测试报告


if __name__=='__main__':

    base_dir = os.path.dirname(os.path.realpath(__file__))  #获取文件当前路径 D:\project\PO\
    test_dir = os.path.join(base_dir,'TestCases')  #D:\project\PO\testCases
    test_report = os.path.join(base_dir,'Reports')  #D:\project\PO\report
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'接口自动化测试框架设计报告',
                            description = u'系统环境:Win10 用例执行情况:')
    runner.run(testlist)
    fp.close()
    new_report = new_file(test_report)   #获取最新报告文件
    send_mail(new_report)                #发送最新的测试报告