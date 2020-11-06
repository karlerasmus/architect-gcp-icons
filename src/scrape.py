import json
from pathlib import Path

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = "https://cloud.google.com/"

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
    if "forward.svg" in src:
        src = "https://www.gstatic.com/cloud/images/navigation/icons.svg#supercloud"
    typ = "img"
    if "svg" in src:
        typ = "svg"

    if src[0] == "/":
        src = url + src
    name = title.string.strip().lower().replace("/","").replace(" ", "_")
    prodList.append({"name": name, "icon": src, "icon-type": typ})

driver.quit()

filePathName = Path.cwd() / "src" / "gcp_products.json"
with open(filePathName, "w") as fp:
    json.dump(prodList, fp, indent=4)
