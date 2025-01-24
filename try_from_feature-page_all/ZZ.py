import requests
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
        html_add = "https://baike.sogou.com" + article_url
        response = requests.get(html_add, timeout=10)
        if response.status_code == 200:     # 状态码200的具体含义：这是最普遍的成功状态码，意味着请求已成功，
                                            # 且所请求的数据包含在响应体中。当服务器返回此状态码时,表明客户端的请求被正确接收、理解和处理。
            bsobj = BeautifulSoup(response.text, 'html.parser')
            print(bsobj.text,'\n', bsobj.title)




            

            # 程序执行到这里，终端显示：“页面 FORBIDDEN 😯”， 后面无法解析网页了！ 







            # 查找所有符合条件的链接
            # 假设链接在具有特定类名的 <a> 标签中，例如 class="lemma-title"
            # 这里需要根据实际情况调整选择器
            # links = bsobj.find_all("a", href=re.compile("^(/sogou/.*|/v/.*)$"))   # 这个正则表达式错误，无法找到东西，  具体啥是正确，要看搜狗百科的URL地址才知道。
            # links = bsobj.find_all("a", href=re.compile("^/v\d+\.htm$"))
            # pattern = r"^/lemma/ShowInnerLink\.htm\?lemmaId=\d+(&.*)?$"
            pattern = r"^/lemma/ShowInnerLink\.htm\?lemmaId="
            links = bsobj.find_all("a", class_='ed_inner_link', href=re.compile(pattern))



            if not links:
                print(f"No links found for {article_url}")
                return []
            
            # 过滤出有效的链接
            valid_links = [link for link in links if 'href' in link.attrs]
            return valid_links
        else:
            print(f"Failed to retrieve page {article_url}, status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error encountered while processing {article_url}: {e}")
        return []

# 记录开始时间
start_time = time.time()

# 初始文章链接，例如“科学”词条
# links = get_links("/v/%E7%A7%91%E5%AD%A6")    # 不要初始文章了，因为找不到东西的，不如为空
links = get_links("/v42423.htm")   # 从“数学”这个词条开始      


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