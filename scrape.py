#import re
import os
import json

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = 'https://cloud.google.com/'

# create a new Chrome session
options = Options()
options.add_argument("--headless")
driver_path = '/home/karl/bin/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=driver_path)

# read page
driver.get(url)

doc = BeautifulSoup(driver.page_source, 'lxml')
products = doc.find_all("div", class_="devsite-nav-item-icon-container") 
prodList = []
for product in products:
    title = product.parent.find('div', class_="devsite-nav-item-title")
    src = product.img['src']
    if src[0] == "/":
        src = url + src
    id = title.string.strip().replace(" ", "-")
    prodList.append({"product": id, "icon": src})

driver.quit()
with open("gcp_products.json", "w") as fp:
    json.dump(prodList, fp, indent=4)
