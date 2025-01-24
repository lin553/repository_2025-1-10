import re
from bs4 import BeautifulSoup

# 示例HTML内容
html_content = '''
<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=237789&amp;ss_c=ssc.citiao.link">笛卡尔</a>
<a class="other_class ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=67890&otherParam=value">无效链接</a>
<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=54321&amp;ss_c=ssc.citiao.link">另一个有效链接</a>
'''

# 解析HTML内容
bsobj = BeautifulSoup(html_content, 'html.parser')

# 定义正则表达式来匹配期望的href属性
pattern = r"^/lemma/ShowInnerLink\.htm\?lemmaId=\d+(&.*)?$"

# 查找所有符合条件的链接
links = bsobj.find_all("a", class_='ed_inner_link', href=re.compile(pattern))

# 输出找到的链接
for link in links:
    print(f"Found link: {link['href']}")