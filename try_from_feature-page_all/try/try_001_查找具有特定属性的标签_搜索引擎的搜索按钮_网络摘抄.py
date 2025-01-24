# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html
from bs4 import BeautifulSoup
import requests

# 指定你想要获取标题的网站
url = 'https://www.baidu.com/' # 抓取bing搜索引擎的网页内容：失败

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, features='html.parser')

# 查找具有 id="unique-id" 的 <input> 标签
unique_input = soup.find('input', id='su')

input_value = unique_input['value'] # 获取 input 输入框的值

print(input_value)