import webbrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global wait
global driver
#wait = WebDriverWait(driver, 40)

url = "https://www.waffarx.com/en-eg"
webbrowser.open(url)

element = driver.find_element(By., "Select Country")