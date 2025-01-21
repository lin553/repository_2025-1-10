# 摘自：通义千问


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 确保使用正确的URL，这里保持原样，但是请注意检查该页面是否含有你想查找的图片
html = urlopen('https://www.eastmoney.com/')
bsobj = BeautifulSoup(html.read(), 'html.parser')   # 在创建 BeautifulSoup 对象时，应该使用 html.read() 获取HTML内容

# 使用一个更通用的正则表达式来匹配图片链接
images = bsobj.find_all('img', {'src': re.compile('.*\.jpg')})  # 匹配所有以.jpg结尾的图片链接

for image in images:
    print(image['src'])