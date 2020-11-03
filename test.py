from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import numpy as np
import subprocess

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=24x24")


def remove_color(img, rgba):


    data = np.array(img.convert('RGBA'))        # rgba array from image
    pixels = data.view(dtype=np.uint32)[..., 0]  # pixels as rgba uint32
    data[..., 3] = np.where(pixels == np.uint32(
        rgba), np.uint8(0), np.uint8(255))  # set alpha channel
    return Image.fromarray(data)


chrome_driver = '/home/karl/bin/chromedriver'
driver = webdriver.Chrome(options=chrome_options,
                          executable_path=chrome_driver)
# driver.get("https://www.gstatic.com/cloud/images/navigation/icons.svg")
driver.get("file:///home/karl/developments/architect-gcp-icons/gcp_icons.svg")
for el in driver.find_elements_by_tag_name("view"):
    product = el.get_property('id')
    print(product) 
    driver.get(f"file:///home/karl/developments/architect-gcp-icons/gcp_icons.svg#{product}")
    driver.execute_script("document.getElementsByTagName('svg')[0].style.zoom = 1.0")
    # take screenshot with a transparent background
    image_path = f"icons/small/{product}.png"
    with Image.open(BytesIO(driver.get_screenshot_as_png())) as img:
        with remove_color(img, 0xffffffff) as img2:                       
            img2.save(image_path)
        
    cmd = ['java', '-Djava.awt.headless=true', 
        '-jar', 
        '/home/karl/Documents/plantuml.1.2020.18.jar',
        '-encodesprite',
        '16z',
        image_path]
    output = subprocess.check_output(cmd, universal_newlines=True)
    print(output)

driver.quit()
