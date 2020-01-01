##2.8  窗口切换实战
from selenium import webdrvier
from time import sleep
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id(“kw”).send_keys(“渗透吧”)
driver.find_element_by_id(“su”).click()
#第一个窗口下点击渗透吧链接
driver.find_element_by_xpath(‘//*[@id="1"]/h3/a’).click()
#使用get获取跳转后的url地址
driver.get(‘http://tieba.baidu.com/f?kw=%C9%F8%CD%B8&fr=ala0&tpl=5’)
sleep(3)
#操作跳转后所在窗口的页面元素
driver.find_element_by_link_text(‘进入贴吧’).click()


###2.8.2  SWITCH方法实战

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
dr = webdriver.Chrome()
url = "https://www.so.com/"
dr.get(url)
sleep(1)
dr.find_element_by_link_text("360导航").click()
sleep(2)
#获取所有窗口的句柄
windows = dr.window_handles
#通过索引切换到第二个窗口
dr.switch_to.window(windows[1])
sleep(0.5)
#在第二个窗口里面文本框内输入 第二个窗口
dr.find_element_by_id("search-kw").send_keys("第二个窗口")
sleep(2)
#切换到第一个窗口