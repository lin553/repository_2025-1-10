from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.eastmoney.com/')    # 东方财富网可抓取
bsobj = BeautifulSoup(html,features="html.parser")
# images = bsobj.findAll('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})   # 原书这段执行后说语法错误！
# images = bsobj.findAll('img',{'src':re.compile('.*\.jpg')})
soups = bsobj.findAll(lambda tag: len(tag.attrs) == 2)

for soup in soups:
    print(soup)