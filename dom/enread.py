import requests
import re
from bs4 import BeautifulSoup

"""
www.enread.com
目标：爬取该网站上的英文文章
"""

# 请求头和代理池
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
	'Cookie': 'bdshare_firstime=1554816397534; PHPSESSID=klu3qka4digl3c7ptua5g0a9h1; yunsuo_session_verify=97a61e192a55a06aa6aca901d627c4ec; Hm_lvt_8e0a0ac35ad5727d6e32afe2a02616e9=1554816399; Hm_lpvt_8e0a0ac35ad5727d6e32afe2a02616e9=1554816546; __tins__1636281=%7B%22sid%22%3A%201554816398968%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201554818346402%7D; __51cke__=; __51laig__=3; srcurl=687474703a2f2f7777772e656e726561642e636f6d2f61642f3534322e68746d6c; security_session_mid_verify=9b8dddb1739baf24c59e4c18d5ce038e',
	'Referer': 'http://www.enread.com/essays/106765.html?security_verify_data=313932302c31303830',
	'Upgrade-Insecure-Requests': '1'
}
proxies = {
	# 'http': 'http://110.52.235.61:9999',
	'https:': 'https://117.85.83.209:53128'
}

url = "http://www.enread.com/essays/106765.html"
response = requests.get(url, headers=headers, proxies=proxies)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('#dede_content > div')
for d in data:
	print(d)
