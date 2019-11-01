import requests
import re
import json
from requests.exceptions import RequestException

def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'gbk'#不设置的话，中文会出现乱码
        return response.text
    print('wrong connection')
    return None

def write_to_file(content):
    with open('yourfilename.txt', 'a', encoding='utf-8') as f:
        f.write(content + '\n')

def parse_one_page(html):
    pattern1 = re.compile('<div id="title">(.*?)</div>',re.S)
    items1 = re.findall(pattern1, html)#标题
    for i in items1:
        write_to_file(i.__str__())
    pattern = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S)
    items2 = re.findall(pattern, html)#内容
    for j in items2:
        write_to_file(j.__str__())
    write_to_file('------------------------------------------------------------------------------\n\n\n')

def main(offset):
    url = 'https://www.wenku8.net/novel/1/1973/'+str(offset)+'.htm'#你的小说网址，自行更改
    html = get_one_page(url)
    parse_one_page(html)

for i in range (101093, 101104):#你的小说哪一章到哪一张的网址，自行更改
    main(i)
