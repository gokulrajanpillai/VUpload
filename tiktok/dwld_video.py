from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time
from bs4 import BeautifulSoup

# Open website

# # Configure driver options
options = webdriver.ChromeOptions()
# options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')   

# # Configure webdriver to accept insecure certificates
# desired_capabilities = {}
# desired_capabilities['acceptInsecureCerts'] = True
# options.set_capability('cloud:options', desired_capabilities)

driver = webdriver.Chrome(options=options)
driver.get("https://www.tiktok.com/@ricoanimations0")

# Wait
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")

videos = soup.find_all("div", {"class": " tiktok-1as5cen-DivWrapper"})

print(len(videos))
for video in videos:
    print(video.a["href"])
