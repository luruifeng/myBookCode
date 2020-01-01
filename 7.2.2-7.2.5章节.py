#6.2.2  发送get请求
import requests
response = requests.get('http://www.baidu.com')
print(r.url)

#6.2.2  发送get请求 带参数
import requests
r = requests.get('http://www.baidu.com/s?',params={'wd':'python'})
print(r.url)


#6.2.3  发送form表单
import requests
payload = {'account':'admin',
           'password':"123456",
           'referer':"http://192.168.0.162:4444/zentao/www/my/"}
r = requests.post('http://192.168.1.116:8011/zentao/www/user-login.html',data=payload,
                  headers={"Content-Type":"application/x-www-form-urlencoded"})
print(r.text)

#6.2.4  发送xml数据
import requests
url  =  'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
payload = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getSupportCityString xmlns="http://WebXml.com.cn/">
      <theRegionCode>3114</theRegionCode>
    </getSupportCityString>
  </soap:Body>
</soap:Envelope>'''
r = requests.post(url=url, data=payload, headers={"Content-Type":"text/xml"})
print(r.text)


####6.2.5  发送json请求

import requests,json

url  = 'http://183.62.166.42:11125/CyzgMobileConfigService/GetDataInfo'
payload = {'CommandCode': 'GetAllCityData',
           'Marker': '1482638389646', "TransferData": "{\'CityId\':4565110}"}
r = requests.post(url=url, json=payload, headers={'Content-Type': 'application/json'})
print(r.text)










