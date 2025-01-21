# 摘自：https://www.runoob.com/python3/python-spider-beautifulsoup.html

import requests

url = 'https://cn.bing.com/'
response = requests.get(url)

# 使用 chardet 自动检测编码， 要使用这个库必须先安装：pip install chardet，我这里就不安装了,所以本程序会报错，正常现象
import chardet
encoding = chardet.detect(response.content)['encoding']
print(encoding)
response.encoding = encoding