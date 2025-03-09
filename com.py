from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json
import urllib.request
import re
from lxml import etree
 
# webservice = 'chromedriver-win64\chromedriver.exe'
# server = Service(webservice)
# driver = webdriver.Chrome(service=server)

url = input('输入漫画地址:')
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)
driver.delete_all_cookies()
with open('cookies.txt','r') as f:
    coolies_list = json.load(f)
    for cookie in coolies_list:
        driver.add_cookie(cookie)
driver.refresh()
name = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[3]/div/div/div[1]/main/section/div[1]/div/figcaption/div[2]/div/h1')

driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[3]/div/div/div[1]/main/section/div[1]/div/div[5]/div/div[2]/button/div[2]').click()
time.sleep(5)
html = driver.page_source
html_H = etree.HTML(html)
html_str = etree.tostring(html_H,encoding='utf-8').decode('utf-8')
pattarn = r'https://i\.pximg\.net/img-master/img/[^\s"]+\.jpg'
urls = re.findall(pattarn,html_str)
print(f'此次下载图片为{len(urls)-1}张')

for url,i in zip(urls,range(len(urls))):
    opener = urllib.request.build_opener()
    opener.addheaders = [('Referer', "https://www.pixiv.net/")]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url,f'img/{name.text}/{i}.jpg')
    print(f'{i}/{len(urls)-1}')
    time.sleep(3)

driver.quit()
print('结束')