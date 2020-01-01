#强制等待

from time import sleep
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
sleep(5)   #强制等待5s
dr.find_element_by_id('kw').send_keys('双击一下')



#隐式等待
from time import sleep
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(30)   #隐式等待设置 30 s
dr.find_element_by_id('kw').send_keys('双击一下')



#显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By   #导入By类
from selenium.webdriver.support.ui import WebDriverWait  #导入WebDriverWait类
from selenium.webdriver.support import expected_conditions as EC  # 导入EC模块
driver = webdriver.Chrome()
driver.get('https://mail.sina.com.cn/')
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID, 'freename')))
element.send_keys('hello')
driver.quit()