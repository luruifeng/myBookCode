###2.13.1  纯文本的邮件实战
import smtplib     #调用smtp发件服务
from email.mime.text import MIMEText    #导入做纯文本的邮件模板类
smtpsever='smtp.qq.com'                #QQ邮箱服务器
sender='qq邮箱账号@qq.com'           #发送者邮箱
psw="hcygozfxeassddhhb"              #配置邮箱客户端生成的QQ邮箱授权码
receiver='126邮箱账号@126.com'       #接收者邮箱
port=465   #QQ邮箱服务器默认端口号

msg=MIMEText(body,'html','utf-8')     #邮件正文内容
msg['from']=qq邮箱账号@qq.com'     #发送者账号
msg['to']='126邮箱账号@qq.com'      #接收者账号
msg['subject'] = "这个是纯文本发送的邮件示例"

smtp = smtplib.SMTP_SSL(smtpsever,port)  #调用发件服务
smtp.login(sender,psw)   #通过发送者的邮箱账号和授权码登录邮箱
smtp.sendmail(sender,receiver,msg.as_string())  #发送邮件，信息以字符串方式保存
smtp.quit()                                   #关闭邮件服务


###2.13.2  带附件的邮件实战
import smtplib
from email.mime.text import MIMEText           #导入做纯文本的邮件模板类
from email.mime.multipart import MIMEMultipart   #导入MIMEMultipart类
#发邮件相关参数
smtpsever='smtp.qq.com'       #QQ邮箱服务器
sender='239xxxxx@qq.com'    #发送者邮箱
psw="xxxxxxxxxxxxxxxx"      #qq邮箱授权码
receiver='xxxxx@126.com'    #接收者邮箱账号
port=465                   #QQ邮箱服务器默认端口号

filepath=r"./readme.txt"  #编辑邮件的内容
with open(filepath,'rb') as fp:    #读文件
    mail_body=fp.read()


#主题
msg=MIMEMultipart()
msg["from"]=sender
msg["to"]=receiver
msg["subject"]="带附件的邮件发送模版主题"

body=MIMEText(mail_body,"html","utf-8")
msg.attach(body)
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)


try:
    smtp=smtplib.SMTP()
    smtp.connect(smtpsever)                     #连接QQ邮箱服务器
    smtp.login(sender,psw)                       #调用发件服务
except:
    smtp=smtplib.SMTP_SSL(smtpsever,port)
    smtp.login(sender,psw)                       #登录邮箱
smtp.sendmail(sender,receiver,msg.as_string())     #发送邮件
smtp.quit()