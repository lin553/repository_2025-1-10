from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('http://pythonscraping.com/pages/page1.html')      # 这个网页已经不能访问了
html = urlopen('http://www.bing.com')
bsobj = BeautifulSoup(html.read(),  features="html.parser") # 如果没有：features="html.parser"  ，vscode会报错：GuessedAtParserWarning：未明确指定解析器，因此我使用的是此系统的最佳可用 HTML 解析器 （“html.parser”）。
                                                                # 这通常不是问题，但如果在另一个系统或不同的虚拟环境中运行此代码，它可能会使用不同的解析器并表现不同。
print(bsobj.h1)