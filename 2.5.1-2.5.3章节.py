###2.5.1 鼠标悬停实战
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  #导入ActionChains类
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
setting = dr.find_element_by_link_text("设置")
ActionChains(dr).move_to_element(setting).perform()
sleep(1)
dr.find_element_by_link_text("搜索设置").click()
sleep(5)


##2.5.2  鼠标右键实战
from selenium.webdriver.common.action_chains import ActionChains  #导入ActionChains类
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
sleep(3)
#定位百度一下按钮元素
context = dr.find_element_by_id('su')
#鼠标悬停右键操作
ActionChains(dr).context_click(context).perform()
sleep(5)


##2.5.3  鼠标双击实战

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  #导入ActionChains类
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
sleep(3)
dr.find_element_by_id('kw').send_keys('双击一下')
#定位百度按钮元素
double = dr.find_element_by_id('su')
#模拟鼠标双击操作
ActionChains(dr).double_click(double).perform()
sleep(5)

