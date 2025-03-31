from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--headless')
# service = Service(ChromeDriverManager().install())
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) # with chrome option

driver.get("http://wikipedia.com")
sleep(2)

# 1 > ID
el1 = driver.find_element(By.ID, 'searchInput')
# print(el1)
# el1.send_keys('Hello world!')

# 2 > Xpath
el2 = driver.find_element(By.XPATH, '//input[@type="search"]')

el3 = driver.find_element(By.XPATH, '//*[text()="Italiano"]')
# el3.click()
# sleep(3)

# 3 > Tag
el4 = driver.find_element(By.TAG_NAME,'select')
# el4.click()
# sleep(3)

# 4 > Link Text
# driver.find_element(By.LINK_TEXT, 'Download Wikipedia for Android or iOS').click()
# sleep(3)

# 5 Partial Link Text
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Download').click()
# sleep(3)


# 6 Class name
# driver.find_element(By.CLASS_NAME, 'sprite svg-search-icon').click()
# sleep(3)

# 7 CSS Selector
el1 = driver.find_element(By.CSS_SELECTOR, '#searchInput').send_keys("Helo")
# driver.find_element(By.CSS_SELECTOR,'.sprite svg-search-icon').click()
sleep(3)
