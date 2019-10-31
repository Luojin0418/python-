import requests
import re
import json
import time
from requests.exceptions import RequestException

def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'gbk'
        return response.text
    print('wrong connection')
    return None

def write_to_file(content):
    with open('11.5爬虫.txt', 'a', encoding='utf-8') as f:
        f.write(content + '\n')

def parse_one_page(html):
    pattern1 = re.compile('<div id="title">(.*?)</div>',re.S)
    items1 = re.findall(pattern1, html)
    for i in items1:
        write_to_file(i.__str__())
    pattern = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
    items2 = re.findall(pattern, html)
    for j in items2:
        write_to_file(j.__str__())
    write_to_file('------------------------------------------------------------------------------\n\n\n')

def main(offset):
    url = 'https://www.wenku8.net/novel/1/1973/'+str(offset)+'.htm'
    html = get_one_page(url)
    parse_one_page(html)

for i in range (101093, 101104):
    main(i)

# this is a test