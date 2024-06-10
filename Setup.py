from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.appiumby import By as MobileBy
#from appium.webdriver.common.touch_action import TouchAction

def setup():
    desired_caps = dict(platformName=  "Android",
  platformVersion =  "10",
  deviceName= "Android SDK built for x86",
  appPackage = "com.waffarx",
  automationName=  "UiAutomator2",
  appActivity=  "com.waffarx.MainActivity")
    global driver
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    # global action
    # action = TouchAction(driver)

    time.sleep(5)
    global wait
    wait = WebDriverWait(driver, 40)

    attempts = 0
    while attempts < 3:
        try:
            Country_List = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Select Country")
            Country_List.click()
            break
        except Exception as e:
            attempts += 1

    time.sleep(0.5)
    Egypt_Choice = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Egypt")
    Egypt_Choice.click()

    time.sleep(0.5)
    Language_List = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Select Language")
    Language_List.click()

    time.sleep(0.5)
    English_Choice = driver.find_element(MobileBy.ACCESSIBILITY_ID, "English")
    English_Choice.click()

    time.sleep(0.5)
    Next_Button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Next >> ")
    Next_Button.click()

    time.sleep(5)
    Close_video = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Next")
    Close_video.click()

    seq=1
    while seq <=2:
        time.sleep(1)
        Arrow_Button = wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.Button')))
        Arrow_Button.click()
        seq+=1

    time.sleep(0.5)
    GetStarted_Button = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Get Started')))
    GetStarted_Button.click()
     #pass     
    return driver, wait
# , action