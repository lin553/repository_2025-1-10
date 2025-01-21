from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("https://www.bing.com")                    # 此网站没有表格数据，访问失败
# html = urlopen('https://finance.sina.com.cn/stock/')        # 此网站没有表格数据，访问失败
html = urlopen('http://www.pythonscraping.com/pages/page3.html')        # 无法连接到此网站
bsobj = BeautifulSoup(html)

for child in bsobj.find("table",{'id':"giftList"}).children:
    print(child)


