# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html

from bs4 import BeautifulSoup
import requests

# 指定你想要获取标题的网站
url = 'https://www.sohu.com/' 

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='html.parser')

# 查找嵌套的 <div> 标签
nested_divs = soup.find_all('div', class_='nested')
for div in nested_divs:
    print(div.get_text())              # 没找到东西