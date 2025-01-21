from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
"""

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 查找第一个<title>标签并打印其文本
print(soup.title.string)

# 查找所有<p>标签并打印它们的class属性
for p in soup.find_all('p'):
    print(p.get('class'))

# 使用CSS选择器找到所有class为sister的<a>标签
links = soup.select('a.sister')
for link in links:
    print(link.get('href'), link.string)