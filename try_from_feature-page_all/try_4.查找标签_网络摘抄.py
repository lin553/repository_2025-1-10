# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html

from bs4 import BeautifulSoup
import requests

# 指定你想要获取标题的网站
url = 'https://www.bing.com/' 

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='html.parser')

# 查找第一个 <a> 标签
first_link = soup.find('a')
print(first_link)
print("----------------------------")

# 获取第一个 <a> 标签的 href 属性
first_link_url = first_link.get('href')
print(first_link_url)
print("----------------------------")

# 查找所有 <a> 标签
all_links = soup.find_all('a')
print(all_links)