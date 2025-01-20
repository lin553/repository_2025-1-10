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

    except AttributeError as e:
        return None
    return bsobj

# bsobj = getTitle('https://sina.com.cn')
# bsobj = getTitle('https://www.amazon.com/-/zh_TW/')
bsobj = getTitle('https://cn.bing.com/dict/search?q=color&FORM=BDVSP2&qpvt=color')
if bsobj is None:
    print("bsobj could not be found")
else:
    nameList = bsobj.findAll('span',{'class':'green'})      # 失败：现在网页没有直接写颜色了，都是找不到了，无论是green、yellow、red都没有。
    print("namelist", nameList)

    if nameList:
        for name in nameList:
            print(name.get_text())
    else:
        print("nameList could not be found")