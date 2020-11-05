from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import numpy as np
import subprocess
import json

driver_path = '/home/karl/bin/chromedriver'

def make_transparent_bgd(img, rgba):
    '''Function to make background transparent'''

    data = np.array(img.convert('RGBA'))        # rgba array from image
    pixels = data.view(dtype=np.uint32)[..., 0]  # pixels as rgba uint32
    data[..., 3] = np.where(pixels == np.uint32(
        rgba), np.uint8(0), np.uint8(255))  # set alpha channel
    return Image.fromarray(data)


with open("gcp_products.json", "r") as fp:
    products = json.load(fp)


sizes = [
    {"size":"small", "img-size": "24", "zoom": "1.0"},
    {"size":"medium", "img-size": "48", "zoom": "2.0"},
    {"size":"large", "img-size": "72", "zoom": "3.0"}
]


for size in sizes:

    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"--window-size={size['img-size']}x{size['img-size']}")

    print(size)

    driver = webdriver.Chrome(options=options, executable_path=driver_path)

    for product in products:
        print(product) 
        
        driver.get(product["icon"])
        if product["icon-type"] == "svg":
            driver.execute_script(f"document.getElementsByTagName('svg')[0].style.zoom = {size['zoom']}")
            driver.execute_script(f"document.getElementsByTagName('svg')[0].style.overflow = 'hidden'")
        else:
            #driver.execute_script(f"document.body.style.zoom = {size['zoom']}") 
            #driver.execute_script("document.body.style.overflow = 'hidden'") 
            driver.execute_script(f"document.getElementsByTagName('img')[0].style.height = {size['img-size']}") 
            driver.execute_script(f"document.getElementsByTagName('img')[0].style.width = {size['img-size']}") 

        # take screenshot with a transparent background
        image_path = f"icons/{size['size']}/{product['name']}.png"
        with Image.open(BytesIO(driver.get_screenshot_as_png())) as img:
            with make_transparent_bgd(img, 0xffffffff) as img2:                       
                img2.save(image_path)
        
    driver.quit()
