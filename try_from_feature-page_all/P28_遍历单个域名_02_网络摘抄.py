# 摘自：通义千问
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 打开网页并读取内容
html = urlopen('https://www.eastmoney.com/')
bsobj = BeautifulSoup(html.read(), features='html.parser')

# 假设你想查找包含在某个div标签下的所有链接，首先需要确定正确的div标识符
# 注意：这里的div选择器应根据实际页面结构调整
div_content = bsobj.find('div', {'id': False})  # 示例选择器，请根据实际情况调整.   id=False: 表示不存在id这个属性

if div_content:
    # 查找所有符合条件的a标签
    for link in div_content.findAll('a', href=re.compile("^https://.*$")):  # 匹配所有以https://开头的链接
        if 'href' in link.attrs:
            print(link.attrs['href'])
else:
    print("指定的div未找到")