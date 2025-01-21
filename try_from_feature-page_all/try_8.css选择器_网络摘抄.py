# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html

from bs4 import BeautifulSoup
import requests

# 指定你想要获取标题的网站
url = 'https://www.eastmoney.com/' 

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='html.parser')

# 使用 CSS 选择器查找所有 class 为 'example' 的 <div> 标签
example_divs = soup.select('div.id')        # 没找到东西

# 查找所有 <a> 标签中的 href 属性
links = soup.select('a[href]')              # 没找到东西