# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html

from bs4 import BeautifulSoup
import requests

# 指定你想要获取标题的网站
url = 'https://www.baidu.com/' 

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='html.parser')
print(soup)
print(type(soup))
print('--------------------------------')

# 转换为字符串
html_str = str(soup)
print(html_str)
print(type(html_str))
print('--------------------------------')

# 格式化并美化文档内容，生成结构化的字符串。
print(soup.prettify())