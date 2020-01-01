#coding=utf-8
#@time   :2018/12/27 22:19
#@Author :Keep Learing
#@boke   :www.cnblogs.com/fighter007
#@motto  :Keep Learing



创建configParser对象cf
cf = configparser.ConfigParser()
# read(filename) 读文件内容
filename = cf.read("config.ini",encoding='utf-8')
print(filename)
# sections() 得到所有的section，以列表形式返回
sec = cf.sections()
print(sec)
# options(section) 得到section下的所有option
opt = cf.options("EMAIL")
print(opt)
# items 得到section的所有键值对
value = cf.items("EMAIL")
print(value)
# get(section,option) 得到section中的option值，返回string/int类型的结果
email_host = cf.get("EMAIL","mail_host")
email_password = cf.get("EMAIL","mail_pass")
email_sender = cf.get('EMAIL','sender')
email_user = cf.get('EMAIL','mail_user')

