import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(1)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://iman.noncd.rz.db.de/psp/pshr/IMAN/IM_LOCAL/h/?tab=DEFAULT")


# close the browser window
#driver.quit()