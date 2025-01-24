from urllib.request import urlopen
from bs4 import BeautifulSoup
import re                           # 正则表达式模块

html = urlopen('https://www.bing.com/')
# html = urlopen('https://www.sohu.com/')     # 搜狐，不可抓取
# html = urlopen('https://www.eastmoney.com/')    # 东方财富网，可抓取
# html = urlopen('https://baike.sogou.com/')

bsobj = BeautifulSoup(html.read(), features='html.parser')


# for link in bsobj.find('div',{'id':'bodyContent'}).findAll('a', href=re.compile("^(/html/)((?!:).)*$")):     # 这是原书代码，但报错，没有 'bodyContent' 这个 'id'
## 正则表达式 ^(/html/)((?!:).)*$ 的含义如下：
## ^: 匹配字符串的开始位置。
## (/html/): 匹配以 /html/ 开头的路径。
## ((?!:).)*: 这是一个复杂的部分：
## (?!:) 是一个负向前瞻断言，表示在当前位置之后不允许出现:字符。
## . 匹配任意单个字符（除了换行符）。
## * 表示前面的模式（即(?!:).）可以重复0次或多次。
## $: 匹配字符串的结束位置。
## 综合起来，这个正则表达式用于匹配那些以 /html/ 开头且后面不包含:字符的所有链接。
## 例如，它会匹配 /html/some/path 但不会匹配 /html:somepath 或者 /html/some:path。


for link in bsobj.find('div',{'id':False}).findAll('a', href=re.compile("^https")):     # id：False 是指筛选不存在id这个项的超链接
    if 'href' in link.attrs:
        print(link.attrs['href'])       # href: 超链接属性


## 用原书代码会失败：什么都没找到，是正则表达式有问题。