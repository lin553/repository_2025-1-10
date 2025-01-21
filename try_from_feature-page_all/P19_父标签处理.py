from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://blog.csdn.net/shuang_waiwai/article/details/131787954") # 网站没有parent属性
bsobj = BeautifulSoup(html)

print(bsobj.find('img',{'src':"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())