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
chrome_options.add_argument('--headless')
# service = Service(ChromeDriverManager().install())
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options) # with chrome option

# Browser action 1 > Open Web
driver.get('https://google.com')

# Browser action 2 > Title
# window_title = driver.title
# print(window_title)
#
# # Browser action 3 > Back
# driver.get('https://wikipedia.com')
# sleep(2)
# driver.back()
# sleep(2)
#
# # Browser Action 4 > Forward
# driver.forward()
# sleep(3)
# # Browser Action 5> Refresh
# driver.refresh()

# Browser Action 6 > Open new window and switch to it (tab
# driver.switch_to.new_window('tab')
# driver.get('https://wikipedia.com')
# sleep(2)

# Browser Action 7 > Open new window and switch to it (window)
# driver.switch_to.new_window('window')
# driver.get("https://yahoo.com")
# sleep(3)

# Browser Action 8 > Current window
# yahoo_window = driver.current_window_handle
# print(f"Yahoo handle" , str(yahoo_window))

# Browser Action 9 > All handles
# all_handle = driver.window_handles
# print("all_handles ", str(all_handle))

# sleep(2)
# driver.find_element(By.NAME, 'q').send_keys('wikipeida')
# sleep(3)
# driver.switch_to.window(all_handle[0])


# Browser action 13 > Window size
# window_size = driver.get_window_size()
# print(window_size)
# width = window_size['width']
# height = window_size['height']
# print(width)
# print(height)

# Browser action 14 > Set Window size
# driver.set_window_size(800,600)
# size = driver.get_window_size()
# print(size)

# Browser Action 15 > get window position
# current_position = driver.get_window_position()
# print(current_position)

# Browser Action 16 > set window position
# driver.set_window_position(100,100)
# sleep(3 )

# Browser Action 17 > Maximize Window
# driver.maximize_window()
# sleep(3)

# Browser action 18 > Fullscreen window
# driver.fullscreen_window()
# sleep(3)

# Browser action 19 > minimize window
# driver.minimize_window()
# sleep(3)

# Browser action 20 > Take Screenshot
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'Thefile.png')
driver.save_screenshot(file_name)

driver.quit()
