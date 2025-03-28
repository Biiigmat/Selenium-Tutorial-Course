from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")  # جلوگیری از شناسایی Selenium

base_url = 'https://play1.automationcamp.ir/'

driver = webdriver.Chrome(options=options)

# driver.get('https://google.com')
#
# # x=input('wef')
# search_field = driver.find_element(By.NAME, 'q')
# search_field.send_keys('Keep it simple stupid')
# search_field.send_keys(Keys.RETURN)
# # x=input()
# sleep(5)

driver.get(f'{base_url}/forms.html')

driver.find_element(By.ID, 'check_python').click()

check1 = driver.find_element(By.ID, 'check_validate').text
assert check1 == "PYTHON"
# sleep(5)X