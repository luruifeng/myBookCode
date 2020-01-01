#-*- coding=utf-8 -*-
__author__ = 'Fighter.Lu'



import time,os,unittest,sys
sys.path.append('./common')
sys.path.append('./basepage')
sys.path.append('./page')
from HTMLTestRunner import HTMLTestRunner  #导入生成邮件测试模版
from homePage import *     #导入基础类
from loginpage import *    #导入页面类
import smtplib  #邮箱服务器
from email.mime.text import MIMEText  #邮件模版类
from email.mime.multipart import MIMEMultipart #邮件附件类
from email.header import Header  #邮件头部模版


#发送带邮件的函数 动作
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    #基本信息
    smtpserver = 'smtp.126.com'
    pwd = "qq123456789" #126邮箱授权码

    #定义邮件主题
    msg=MIMEMultipart()
    msg['subject'] = Header(u'Page Object自动化测试报告','utf-8')
    msg['from'] = "luruifengx@126.com"    #必须加 不加报错  发送者的邮箱
    msg['to'] =  "luruifengx@126.com"     #必须加 不加报错  接收者的邮箱

    #不加msg['to'] msg['from']报错原因，是因为“发件人和收件人参数没有进行定义

    #HTML邮件正文 直接发送附件的代码片段
    body=MIMEText(mail_body,"html","utf-8")
    msg.attach(body)
    att = MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
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
    file_path = os.path.join(result_dir,file[-1])     #找到测试报告目录下面最新的测试报告
    return file_path  #返回最新的测试报告

if __name__=='__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))  #获取文件所在路径
    test_dir = os.path.join(base_dir,'TestCases')  #测试用例所在目录
    test_report = os.path.join(base_dir,'report')  #测试报告所在目录
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + "\\" + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = u'PageObject自动化测试报告',
                            description = u'系统环境:Win10 浏览器:Chrome 用例执行情况:')
    runner.run(testlist)
    fp.close()

    new_report = new_file(test_report)   #获取最新报告文件
    send_mail(new_report)                #发送最新的测试报告


#实现的逻辑
#1.先生成测试报告
#2.查找最新的测试报告 通过new_file函数 找到最新的测试报告 作为一个结果返回 file_path
#3.把new_file函数 找到最新的测试报告 file_path (最新的测试报告) 以邮件附件的形式加载到邮件模版中 设置参数  连接邮箱服务器发送最新的测试报告
