####2.3.1  单个元素定位

# 1.通过find_element_by_id定位
# 示例如下：
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys('大道至简')
# 2.通过find_element_by_name定位
# 示例如下：
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_name("kw").send_keys('大道至简')
driver.quit()
# 3.通过find_element_by_class_name定位
# 示例如下：
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_class_name("s_ipt").send_keys('大道至简')
driver.quit()



#2.3.2 多个元素定位实战
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('file:///' + os.path.abspath('checkbox.html'))
driver.find_elements_by_css_selector("input[type='checkbox']")[0].click()
driver.quit()


#2.3.3  By类定位
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
tag = dr.find_elements_by_tag_name('input')
for t in tag:
if t.get_attribute('autocomplete') == 'off':
t.send_keys('fighter007')
driver.find_element_by_id('su').click()
dr.quit()

#2.3.4 js定位
from selenium import webdriver
import time as t
dr = webdriver.Chrome()
dr.get('https://www.jianshu.com/sign_in')
t.sleep(2)
#点击注册按钮
js_register = 'document.getElementById("js-sign-up-btn").click();'
dr.execute_script(js_register)
t.sleep(2)

#2.3.5 jquery定位
#定位登录连接
js_class = 'document.getElementsByClassName("active")[0].click();'
dr.execute_script(js_class)
t.sleep(2)
#定位账号文本框  输入username
js_input='document.getElementsByTagName("input")[2].value="username";' dr.execute_script(js_input)
t.sleep(2)
#定位密码文本框 输入password
# js_passwd = 'document.getElementsByTagName("input")[3].value="password";'
dr.execute_script(js_passwd)
t.sleep(2)
#使用css选择器定位 登录按钮
css_btn = 'document.querySelectorAll(".sign-in-button")[0].click();'
dr.execute_script(css_btn)

