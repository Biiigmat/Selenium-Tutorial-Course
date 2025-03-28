from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Browser action 1 > Open Web
driver.get('https://google.com')

# Browser action 2 > Title
window_title = driver.title
print(window_title)

# Browser action 3 > Back
driver.get('https://wikipedia.com')
sleep(2)
driver.back()
sleep(2)

# Browser Action 4 > Forward
driver.forward()
sleep(3)
# Browser Action 5> Refresh
driver.refresh()

# Browser Action 6 > Open new window and switch to it (tab
driver.switch_to.new_window('tab')
sleep(2)

# Browser Action 6 > Open new window and switch to it (window)
driver.switch_to.new_window('window')
sleep(3)

# sleep(2)
# driver.find_element(By.NAME, 'q').send_keys('wikipeida')
# sleep(3)
# driver.quit()
