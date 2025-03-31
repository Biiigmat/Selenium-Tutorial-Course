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
chrome_options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://play1.automationcamp.ir/forms.html')
sleep(3)

download_link = driver.find_element(By.ID, 'download_file')

download_link.click()
sleep(5)

file_name ='sample_text.txt'

downloads_folder = os.path.join(os.path.expanduser('~'), "Downloads")
file_path = os.path.join(downloads_folder,file_name)

if os.path.exists(file_path):
    print("Download was Successfull! ")
else:
    print("Download was not Successfull! ")
driver.quit()


