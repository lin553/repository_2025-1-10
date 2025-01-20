from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read(),  features="html.parser") # 如果没有：features="html.parser"  ，vscode会报错：GuessedAtParserWarning：未明确指定解析器，因此我使用的是此系统的最佳可用 HTML 解析器 （“html.parser”）。
                                                                        # 这通常不是问题，但如果在另一个系统或不同的虚拟环境中运行此代码，它可能会使用不同的解析器并表现不同。
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

# title = getTitle("https://www.amazon.com/-/zh_TW/")
title = getTitle('https://www.bing.com')
if title == None:
    print("title could not be found")
else:
    print(title)