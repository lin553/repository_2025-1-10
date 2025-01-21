from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('https://www.bing.com/')
# html = urlopen('https://www.sohu.com/')     # 搜狐，不可抓取
html = urlopen('https://www.eastmoney.com/')    # 东方财富网，可抓取

bsobj = BeautifulSoup(html.read(), features='html.parser')

for link in bsobj.findAll('a'):         # 所有包含"a"的元素
    if 'href' in link.attrs:
        print(link.attrs['href'])       # href: 超链接属性