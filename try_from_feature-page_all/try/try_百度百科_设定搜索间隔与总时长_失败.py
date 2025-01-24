from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import time  # 导入time模块用于设置延时

# 设置随机种子
random.seed(int(datetime.datetime.now().timestamp()))

# 设置请求间隔（秒）
request_interval = 2  # 每次请求后等待2秒

# 设置最大执行时长（秒）
max_execution_time = 60  # 脚本最长运行时间为60秒

def get_links(article_url):
    try:
        html = urlopen("https://baike.baidu.com" + article_url)
        bsobj = BeautifulSoup(html.read(), 'html.parser')
        
        # 根据百度百科的实际HTML结构调整选择器
        return bsobj.find("div", {'class': 'main-content'}).findAll("a", href=re.compile("^(/item/)((?!:).)*$"))
    except Exception as e:
        print(f"Error encountered while processing {article_url}: {e}")
        return []

# 记录开始时间
start_time = time.time()

# 初始文章链接，例如“科学”词条
links = get_links("/item/%E7%A7%91%E5%AD%A6")

while len(links) > 0:
    current_time = time.time()
    if (current_time - start_time) > max_execution_time:
        print("Maximum execution time reached. Exiting.")
        break
    
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    
    # 在下一次请求前暂停指定秒数
    time.sleep(request_interval)
    
    links = get_links(new_article)