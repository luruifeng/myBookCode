##2.16.3  多线程调用浏览器运行实战

from selenium import webdriver
from time import sleep
import threading    #导入多线程模块
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
def  test_baidu_search(browser,url):
    if   browser == "FireFox":
        # 创建的新实例驱动
        options = webdriver.FirefoxOptions()
        # 火狐无头模式
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        executable_path = r'C:\Python36\geckodriver.exe'
        driver = webdriver.Firefox(firefox_options=options, executable_path=executable_path)
        # driver = webdriver.Firefox()
    elif browser == "Chrome":
        # 创建的新实例驱动
        chrome_options = Options()
        # 谷歌无头模式
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver = webdriver.Chrome()
    elif browser == 'Ie':
        driver = webdriver.Ie()
    #搜索脚本
    driver.get(url)
    sleep(3)
    driver.find_element_by_id("kw").send_keys(u"多线程启动不同浏览器")
    driver.find_element_by_id("su").click()
    sleep(3)
    driver.quit()

if __name__ == "__main__":
    data = {"FireFox": "http://www.baidu.com","Chrome": "http://www.baidu.com",
            "Ie":"http://www.baidu.com"}
    #构建线程
    threads = [ ]
    for browser, url in data.items():
        t = threading.Thread(target=test_baidu_search, args=(browser, url))
        threads.append(t)
    #启动所有线程
    for thr in threads:
        thr.start()