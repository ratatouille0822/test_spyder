from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
input_
print(browser.page_source)
browser.close()



