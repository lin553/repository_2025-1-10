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
print('\n', first_link['href'])
print('----------------')

# 修改第一个 <a> 标签的 href 属性
first_link['href'] = 'http://new-url.com'
print(first_link['href'])


print('===================')
# 修改第一个 <p> 标签的文本内容
first_paragraph = soup.find('p')
print(first_paragraph)
print('----------------')
first_paragraph.string = 'Updated content'
print(first_paragraph)

print('===================')
# 删除某个标签
first_paragraph.decompose()
print(first_paragraph.string)