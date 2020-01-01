#2.4.1 下拉框定位  value属性定位
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
dr = webdriver.Chrome()
url = dr.get("file:///D:/xialakuang.html")
element = dr.find_element(By.ID,"s1Id")
Select(element).select_by_value("o1")


#2.4.2下拉框   index属性定位
from selenium import webdriver
from selenium.webdriver.common.by import By #引入By类
from selenium.webdriver.support.ui import Select  #引入Select类
from time import sleep
dr = webdriver.Chrome()
url = dr.get("file:///D:/xialakuang.html")
element = dr.find_element(By.ID,"s4Id")
Select(element).select_by_index(1)


###2.4.3  visible_text属性定位
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
dr = webdriver.Chrome()
url = dr.get("file:///D:/xialakuang.html")
element = dr.find_element(By.ID,"s4Id")
Select(element).select_by_visible_text("o3"）



# 2.4.4  元素二次定位实战
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
url = dr.get("file:///D:/xialakuang.html")
dr.find_element_by_id("s4Id").find_element_by_xpath("//*[@id=’id2]’).click()


