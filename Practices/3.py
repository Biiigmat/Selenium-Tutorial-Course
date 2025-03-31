import os.path

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = Options()
# chrome_options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service) #options=chrome_options)

driver.get('https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_text')

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframeResult')))

driver.find_element(By.ID, 'fname').send_keys('Matin')
driver.find_element(By.ID, 'lname').send_keys('Moeinpour')
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'w3-container')))

# پیدا کردن و استخراج محتوای div
div_result = driver.find_element(By.CSS_SELECTOR, '.w3-container.w3-large.w3-border')
print(div_result.text)
sleep(5)



