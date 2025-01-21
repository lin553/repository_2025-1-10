# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html

from bs4 import BeautifulSoup
import requests

# 指定你想要获取标题的网站
url = 'https://www.baidu.com/' # 抓取bing搜索引擎的网页内容

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='html.parser')

# 获取第一个 <p> 标签中的文本内容
paragraph_text = soup.find('p').get_text()
print(paragraph_text)
print('-------------------')
# 获取页面中所有文本内容
all_text = soup.get_text()
print(all_text)