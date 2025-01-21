from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置正确的驱动路径
service = ChromeService(executable_path="/RUNOOB/Downloads/chromedriver-mac-arm64/chromedriver") 
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


# 打开一个网站
driver.get("https://cn.bing.com")

# 获取页面标题
print(driver.title)

# 关闭浏览器
driver.quit()