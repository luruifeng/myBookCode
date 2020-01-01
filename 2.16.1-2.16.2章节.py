#####2.16.1  配置Firefox无头模式

from selenium import webdriver
#创建新实例
options=webdriver.FirefoxOptions()
#设置火狐无头模式     
options.add_argument('--headless')
options.add_argument('--disable-gpu')
executable_path=r'C:\Python36\geckodriver.exe'  #火狐驱动所在路径
driver=webdriver.Firefox(firefox_options=options,executable_path=executable_path) 


#####2.16.2  配置Chrome无头模式

from selenium import webdriver
#创建新实例
chrome_options = Options()
#设置谷歌无头模式     
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=options,options=chrome_options)