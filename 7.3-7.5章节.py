####6.3  处理 token 

import requests
url = 'http://212.123.456.123:1112/login'
data = {'username':'admin','password':'admin'}
response = requests.post(url=url,json=data,
                         headers={'Content-Type':"application/json"})
print(response.json())


###6.4  处理 cookie

def login():
   '''登录禅道获取登录后的session'''
   r=requests.post('url=http://192.168.0.162:4444/zentao/www/user-login.html',
                   data={'account':'admin',
                    'password':'123456',
                    'referer':"http://192.168.0.162:4444/zentao/www/my/"})
   return r.cookies
   
def ViewBug():
   '''查看bug单'''
   r = requests.get(url='http://192.168.0.162:4444/zentao/www/my-bug.html',cookies=login())
   return r.text
print(ViewBug())


###6.5  处理 session
import requests

data = {
    "email":"18513600xxx",
    "icode":"",
    "origURL":"http://www.renren.com/home",
    "domain":"renren.com",
    "key_id":1,
    "captcha_type":"web_login",
    "password":"403ebf9eelri59d8df30669206e8885236klaece4884c0cca4642365b0e4096a",
    "rkey":"41602f6afc3b0686fd38866f4cd6d5c8",
    "f":""}
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181131458439'
def  RenrenLogin():
    '''登陆接口'''
    s = requests.Session()
    r = s.post(url=url,data=data)
    return  s


###6.5  处理 session