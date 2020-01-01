import requests  #导入requests库

response = requests.get(url='http://www.baidu.com',timeout=0.001)
print(response.text)