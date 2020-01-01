##2.10.1 JavaScript实战
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get(“http://localhost:8080”)
#定位富文本 并向富文本输入内容 A
js="document.getElementById('content_ifr').contentWindow.document.body.innerHTML='%s'" %(A)
driver.execute_script(js)


##2.10.2  处理隐藏元素实战

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
dr = webdriver.Chrome()
dr.get('file:///E:/webdriver_api_demo/frame.html')
sleep(2)
#设置元素为可见
js = 'document.querySelectorAll("select")[0].style.display="block";'
dr.execute_script(js)
sleep(3)
element = dr.find_element(By.ID,"s3")
Select(element).select_by_visible_text("po设计模式")


##2.10.3  处理readonly属性实战
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get('https://kyfw.12306.cn/otn/leftTicket/init')
sleep(2)
js1 = "document.getElementById('train_date').removeAttribute('readonly');"  #移除readonly属性
dr.execute_script(js1)
sleep(2)
dr.find_element_by_id('train_date').clear()   #清空日期
dr.find_element_by_id('train_date').send_keys('2018-12-10')  #输入最新日期

##2.10.4  处理浏览器滚动条实战

from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")  #访问百度搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)
driver.execute_script("window.scrollTo(0,10000);") #将页面滚动条拖到底部
sleep(3)
driver.execute_script("window.scrollTo(10000,0);")  #将滚动条移动到页面的顶部
sleep(3)
driver.quit()




from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys   #引入键盘类
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")  #访问百度搜索
driver.find_element_by_id("kw").send_keys("好奇心日报")
driver.find_element_by_id("su").click()
sleep(5)
#将页面滚动条拖到底部
driver.find_element_by_xpath('//*[@id="page"]/a[10]').send_keys(Keys.DOWN)
sleep(5)
#将滚动条移动到页面的顶部
driver.find_element_by_xpath('//*[@id="s_tab"]/div/a[9]').send_keys(Keys.UP)
sleep(5)
driver.quit()




