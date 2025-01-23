from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re   # 正则表达式库

random.seed(datetime.datetime.now())    # 随机种子

def getlinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsobj = BeautifulSoup(html,features='html.parser')
    return bsobj.find("div",{'id':'bodyContent'}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getlinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getlinks(newArticle)