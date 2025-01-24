# 成功：2025-1-24，当前baike.baidu.com网页的格式是这样的：含新词条的内部链接的类名是：{'class': 'innerLink_s8pNv'}  词条首词格式是以 item 开头。

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import time

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
        
        # 查找所有符合条件的链接
        # 这里我们不指定特定的div容器，而是直接在整个文档中查找
        links = bsobj.findAll("a", {'class': 'innerLink_s8pNv'}, href=re.compile("^/item/"))
        if not links:
            print(f"No links found for {article_url}")
            return []
        
        # 提取href属性值，并过滤掉重复的链接
        # 这里link['href] 只有百科的内部链接，即：不包含："https://baike.baidu.com"前缀
        valid_links = list(set([link['href'] for link in links if 'href' in link.attrs]))       # set(): 创建一个无序且不重复元素的集合
                                                                                                
        return valid_links
    except Exception as e:
        print(f"Error encountered while processing {article_url}: {e}")
        return []

# 记录开始时间
start_time = time.time()

# 初始文章链接
links = get_links("/item/%e6%95%b0%e5%ad%a6")   # 从“数学”开始找， 不能从空字符开始，因为百度百科的首页没多少链接，也没item开头的链接 

while len(links) > 0:
    current_time = time.time()
    if (current_time - start_time) > max_execution_time:
        print("Maximum execution time reached. Exiting.")
        break
    
    new_article = links[random.randint(0, len(links)-1)]
    print(new_article)
    
    # 在下一次请求前暂停指定秒数
    time.sleep(request_interval)
    
    links = get_links(new_article)             