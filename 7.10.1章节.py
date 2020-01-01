import json  #导入json库
#定义字典
dict1={'name':"fighter",
      'age':28,
      'address':'shenzhen'}
print ('未序列化前的数据类型为:',type(dict1))
print ('未序列化前的数据:',dict1)
#对python对象进行序列化操作
print ('begin对python对象进行序列化操作------------>')
str1 = json.dumps(dict1)
print ('序列化后的数据类型为:',type(str1))
print ('序列化后的数据为:',str1)
#对str1进行反序列化操作
print ('begin对str1对象进行反序列化操作------------>')
dict2 = json.loads(str1)
print ('反序列化后的数据类型:',type(dict2))
print ('反序列化后的数据:',dict2)