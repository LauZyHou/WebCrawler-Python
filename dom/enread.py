import requests
import re
from bs4 import BeautifulSoup

"""
www.enread.com
目标：爬取该网站上的英文文章
"""

# 请求头和代理池,请求不到了就更新一下Cookie和Referer和代理
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
	'Cookie': 'bdshare_firstime=1554816397534; yunsuo_session_verify=a3592d2ac8137fec7a5b9e7966e9a915; Hm_lvt_8e0a0ac35ad5727d6e32afe2a02616e9=1554816399,1554900527; Hm_lpvt_8e0a0ac35ad5727d6e32afe2a02616e9=1554900527; __tins__1636281=%7B%22sid%22%3A%201554900527525%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201554902327525%7D; __51cke__=; __51laig__=1; srcurl=687474703a2f2f7777772e656e726561642e636f6d2f6573736179732f3130363736352e68746d6c; security_session_mid_verify=f98f1b0f19079f7c9eac26fe2586a6cf',
	'Referer': 'http://www.enread.com/essays/106765.html?security_verify_article=313932302c31303830',
	'Upgrade-Insecure-Requests': '1'
}
proxies = {
	# 'http': 'http://110.52.235.61:9999',
	'https:': 'https://117.85.83.209:53128'
}

url = "http://www.enread.com/essays/106765.html"
article = head = None
max_cnt = 4  # 一个页面的最大尝试次数

# 网站做了保护,请求为空就再请求几次试试
while (not head or not article) and max_cnt > 0:
	response = requests.get(url, headers=headers, proxies=proxies)
	soup = BeautifulSoup(response.text, 'lxml')
	head = soup.select(
		'#wenzhangziti > table > tbody > tr:nth-of-type(1) > td > table > tbody > tr:nth-of-type(1) > td > div > font')
	article = soup.select('#dede_content > div')
	max_cnt -= 1
if (not head) or len(head)==0:
	print("获取失败")
else:
	# 处理标题
	head = re.sub(r'</{0,1}\w.*?>', "", str(head[0]))
	# todo 文章标题持久化到数据库
	print(head)
	with open("./data/text.txt", 'w', encoding='utf8') as f:
		# 处理文章的逐段内容,并写入文件
		for d in article:
			# 匹配HTML标签并替换空串以将其删除
			d = re.sub(r'(<a href="#_w_\d+">\d+</a>)|(</{0,1}\w.*?>)', "", str(d))
			# 去除首尾空白(因为可能有大量空白)
			d = d.strip()
			if len(d) > 0:
				f.write(d)
				f.write("\n\n")


"""
用下面的小片段测试正则匹配
It was pretty <a href="http://dict.qsbdc.com/devastating" target="_blank">6<strong class="arc_point">devastating<sup class="circle"><a href="#_w_5">5 because other children constantly ma</div><a href="#_w_1">1</a>
"""