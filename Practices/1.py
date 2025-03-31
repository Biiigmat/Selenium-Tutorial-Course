from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://play1.automationcamp.ir/forms.html')

check_python = driver.find_element(By.ID, 'check_python')
check_validate = driver.find_element(By.ID, 'check_validate')
if check_python.is_enabled():
    check_python.click()
    print('Button is enabled')
else:
    print('Button is disabled')

driver.quit()
