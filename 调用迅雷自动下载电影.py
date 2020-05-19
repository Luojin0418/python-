from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
import re
import math
# import warnings

# warnings.filterwarnings('ignore')

# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
# # chrome_options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36)'")
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_options.add_experimental_option("prefs",prefs)
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1124, 850)
wait = WebDriverWait(browser, 5)

name = input('请输入需要下载的电影或电视剧：')
browser.get("https://www.dygod.net/")
nameinput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".searchl [name='keyboard']")))

nameinput.send_keys(name)
search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".searchr [name = 'Submit']")))
search.click()

print("搜索到的结果：\n")
browser.switch_to.window(browser.window_handles[1])
# print(browser.page_source)
result = browser.find_elements_by_css_selector('.co_content8 table a')
more = browser.find_elements_by_css_selector('.co_content8 .x')
# print(result)

if result:
    sign = 0
    all_href = []
    for i in result:
        title = i.text
        href = i.get_attribute('href')
        all_href.append(href)
        print(str(sign) + ':   ' + title)
        sign = sign+1
else:
    print("没有找到相关内容")

if more:
    total = more[0].find_element_by_css_selector('[title=总数]').text
    now_page = more[0].find_elements_by_css_selector(':not(a)')
    all_page = math.ceil(int(total)/20)
    print()
    print("共查找到%d个结果，当前展示的是第%d面，共有%d面" %(int(total),int(now_page[1].text),int(all_page)))
    print('若无想要的结果，请换一个关键词查询！')


# sign = 0
# all_href = []
# for i in result:
#     title = i.text
#     href = i.get_attribute('href')
#     all_href.append(href)
#     print(str(sign) + ':   ' + title)
#     sign = sign+1 

num = input("请输入需要查看的链接：")
browser.get(all_href[int(num)])

film = browser.find_element_by_css_selector('#Zoom')
film_intro = re.findall('简　　介\n([\w\W]*?)\n◎',film.text,re.S)
print('简介：')
print(film_intro)

temp = browser.find_elements_by_css_selector('#Zoom tbody a')
film_download = []
sign_url = 0
for i in temp:
    print(str(sign_url) + ':   ' + i.text)
    film_download.append(i.get_attribute('href'))
    sign_url = sign_url+1

num1 = input("请输入需要下载的编号：")
os.chdir("E:\\ThunderX_10.1.2.174_Portable\\ThunderX\\Program")
os.system("Thunder.exe -StartType:DesktopIcon \"%s\"" % film_download[int(num1)])

browser.close()
