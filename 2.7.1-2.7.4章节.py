###2.7.1表单切换实战
from selenium import webdrvier
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
time.sleep(2)
driver.switch_to.frame('login_frame')   #切换iframe标签
driver.find_element_by_name("email").send_keys('username')
driver.find_element_by_name("password").send_keys('password')
driver.find_element_by_id("login_button").click()
driver.switch_to.default_content()  #退出iframe标签





###2.7.2 嵌套表单切换 平行表单切换实战

from selenium import webdrvier
driver = webdriver.Chrome()
driver.get('file:///E:/webdriver_api_demo/frame.html')
time.sleep(2)
#先切换到最外层的iframe标签
driver.switch_to.frame('f1')   
#再切换到第二个iframe标签
driver.switch_to.frame('f2')
#定位处在第二个iframe标签中的元素
driver.find_element_by_name("email").send_keys('username')

### 2.7.3 
from selenium import webdrvier
driver = webdriver.Chrome()
driver.get('file:///E:/webdriver_api_demo/frame.html')
time.sleep(2)
#默认在iframe1标签
driver.switch_to.frame('osslog_iframe')   
#退出iframe1标签
driver.switch_to.default_content()  #退出iframe标签
#切换到iframe2标签
driver.switch_to.frame('actionFrame')
#操作iframe2标签下面的元素
driver.find_element_by_name("email").send_keys('username')


###2.7.4 表单特殊情况处理

from selenium import webdrvier
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
time.sleep(2)
#使用xpath层级定位iframe标签
Xpath=driver.find_element_by_xpath("//div[@id=’QMEditorArea’]/table/tbody/tr[2]/td/iframe")
driver.switch_to.frame(Xpath)   #切换到iframe标签
driver.find_element_by_name("email").send_keys('username')
driver.find_element_by_name("password").send_keys('password')
driver.find_element_by_id("login_button").click()