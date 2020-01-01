#7.11  XML与JSON数据之间的转换

import json
import xmltodict
#定义xml转json的函数
def xmltojson(xmlstr):
  xmlparse = xmltodict.parse(xmlstr)    #parse是的xml解析器
  jsonstr = json.dumps(xmlparse,indent=2,sort_keys=True)
  print(jsonstr)

if __name__ == '__main__':
  xmlinfo = """<student>
    <bokeid>fighter006</bokeid>
    <bokeinfo>
      <cnbologsname>laolu</cnbologsname>
      <page>230</page>
    </bokeinfo>
    <date>
      <address>http://www.baidu.com</address>
      <title>python+ddt+requests</title>
    </date>
  </student>
    """
  xmltojson(xmlinfo)