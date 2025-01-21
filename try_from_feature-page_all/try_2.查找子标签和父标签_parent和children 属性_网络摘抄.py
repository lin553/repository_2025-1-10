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

# 查找第一个 <a> 标签
first_link = soup.find('a')
print(first_link)
print("----------------------------")

# 获取当前标签的父标签
parent_tag = first_link.parent
print(parent_tag.get_text())



print("----------------------------")
# 获取当前标签的所有子标签
childrens = first_link.children
for children in childrens:
    print(children.get_text())