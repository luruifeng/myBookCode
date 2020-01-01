###7.7  Response对象解析
import requests 
r = requests.get('http://httpbin.org/get')

print('HTTP状态码:',r.status_code)  #响应状态码 常见 200 301 302 404 500 
print('返回原始响应体',r.raw)
print('请求的响应体',r.content)  #字节方式的响应体，会自动解码gzip和deflate 压缩
print('响应内容',r.text)         #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print('获取headers',r.headers)  #以字典对象存储服务器响应头
print(r.json())    #Requests中内置的 Json 解码器 将响应结果转换为JSON字符串
print(r.raise_for_status())   #失败请求(非200 响应)抛出异常