
# 2.9  警告框实战

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.select import Select
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
setting = dr.find_element_by_link_text("设置")
ActionChains(dr).move_to_element(setting).perform()
sleep(1)
dr.find_element_by_link_text("搜索设置").click()
sleep(5)
# 选择简体中文
dr.find_element_by_id("SL_1").click()
sleep(3)
# 下拉框的操作
select = dr.find_element_by_xpath("//select[@id='nr']")
Select(select).select_by_value("20")
sleep(3)
# 保存设置
dr.find_element_by_class_name("prefpanelgo").click()
# 处理警告框
alert = dr.switch_to.alert
# 打印警告信息
print(alert.text)