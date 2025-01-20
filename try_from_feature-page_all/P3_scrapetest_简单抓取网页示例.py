# P3_简单抓取网页示例

from urllib.request import urlopen

# html = urlopen('http://pythonscraping.com/pages/page1.html')      # 这个网页已经不能访问了
# html = urlopen('https://www.amazon.com/-/zh_TW/')
html = urlopen('http://www.bing.com')
print(html.read())
