import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

webservice = Service('chromedriver-win64\chromedriver.exe')
html = webdriver.Chrome(service=webservice)

html.get('http://pixiv.net/')
time.sleep(160)
with open('cookies.txt','w') as f:
    f.write(json.dumps(html.get_cookies()))
html.close()




