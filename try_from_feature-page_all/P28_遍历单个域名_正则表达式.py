from urllib.request import urlopen
from bs4 import BeautifulSoup
import re                           # 正则表达式模块

html = urlopen('https://www.bing.com/')
# html = urlopen('https://www.sohu.com/')     # 搜狐，不可抓取
# html = urlopen('https://www.eastmoney.com/')    # 东方财富网，可抓取

bsobj = BeautifulSoup(html.read(), features='html.parser')

# for link in bsobj.find('div',{'id':'bodyContent'}).findAll('a', href=re.compile("^(/html/)((?!:).)*$")):     # 这是原书代码，但报错，没有 'bodyContent' 这个 'id'
for link in bsobj.find('div',{'id':False}).findAll('a', href=re.compile("^(/html/)((?!:).)*$")):     # id：False 是指筛选不存在id这个项的超链接
    if 'href' in link.attrs:
        print(link.attrs['href'])       # href: 超链接属性




# 失败, 
# 啥都没找到，我猜是正则表达式问题，用网络摘抄的成功了。