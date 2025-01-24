# 失败，中国打不开wiki

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random

random.seed(datetime.datetime.now().timestamp())  # 设置随机种子

def get_links(article_url):
    try:
        html = urlopen("https://en.wikipedia.org" + article_url)
        bsobj = BeautifulSoup(html.read(), 'html.parser')
        return bsobj.find("div", {'id': 'bodyContent'}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except Exception as e:
        print(f"Error encountered while processing {article_url}: {e}")
        return []

links = get_links("/wiki/Kevin_Bacon")

while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    links = get_links(new_article)