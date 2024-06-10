from appium.webdriver.common.appiumby import By as MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from Setup import setup

x = 300
y = 300

def HomePage():
    driver, wait = setup()
    #, action 
    LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
    LoginButton.click()

    Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
    Email.click()
    Email.clear()
    Email.send_keys("gnohair@gmail.com")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')

    time.sleep(2)
    Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Password.click()
    Password.clear()
    Password.send_keys("Ng555555")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

    Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
    Login.click()

    #time.sleep(2)
    #action.tap(x=x, y=y).perform()  # to click on any position on screen

    print("\n\n" + "*"*50)
    print(" "*5 + " Home page:: Online Top stores Test Cases " + " "*15)
    print("*"*50 +"\n")

    # Amazon = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Amazon.eg")
    # Amazon.click()
    # assert "Cash Back Categories" in driver.page_source
    # print("\033[32mCheck that page of store details open when click on logo of store:: Passed\033[0m")

    # back = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button')))
    # back.click()

    time.sleep(5)
    OnlineTopStores_See_All = driver.find_element(MobileBy.ACCESSIBILITY_ID, "See All")
    OnlineTopStores_See_All.click()

    # #See_All_Title = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Online Top Stores")
    # assert "Online Top Stores" in driver.page_source
    # print("\033[32mCheck that title of page see all is correct:: Passed\033[0m")

    # RedPercentage = wait.until(EC.presence_of_element_located((By.XPATH,'(//android.view.View[@content-desc="Up to 7.00%"])[1]')))
    # RedPercentage.click()
    # assert "Proceed to Amazon.eg" in driver.page_source
    # print("\033[32mCheck that popup of exit click appear when click on RedPercentage:: Passed\033[0m")

# def Favourite_stores():
#     driver, wait = setup()
#     #, action 
#     LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
#     LoginButton.click()

#     Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
#     Email.click()
#     Email.clear()
#     Email.send_keys("gnohair@gmail.com")

#     time.sleep(1)
#     driver.hide_keyboard(strategy='pressKey', key='Done')

#     time.sleep(1)
#     Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
#     Password.click()
#     Password.clear()
#     Password.send_keys("Ng555555")

#     time.sleep(1)
#     driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

#     Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
#     Login.click()

#     #driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Akash").instance(0))').click()
#     # This above line to refresh page

#     print("\n\n" + "*"*50)
#     print(" "*5 + " Home page:: Favourite stores Test Cases " + " "*15)
#     print("*"*50 +"\n")

#     ##############  Check that store added correctly when click on it and click done ##############
#     AddStore = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Add Store")
#     AddStore.click()
#     assert "Favourite Stores" in driver.page_source
#     print("\033[32mCheck that title of page favourite Stores is correct:: Passed\033[0m")

#     Store_Beddinginn = wait.until(EC.presence_of_element_located((By.XPATH,'//android.view.View[@content-desc="Beddinginn"]/android.view.View')))
#     Store_Beddinginn.click()
#     Done_Button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Done")
#     Done_Button.click()

#     assert "Beddinginn" in driver.page_source
#     print("\033[32mCheck that store added correctly when click on it and click done:: Passed\033[0m")

#     ##############  Check that store added correctly when click on it and click back ##############

#     AddStore = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Add Store")
#     AddStore.click()

#     Store_CruiseDirect = wait.until(EC.presence_of_element_located((By.XPATH,'//android.view.View[@content-desc="CruiseDirect"]/android.view.View')))
#     Store_CruiseDirect.click()
#     Back_Button = driver.find_element(MobileBy.CLASS_NAME, "android.widget.Button")
#     Back_Button.click()

#     assert "CruiseDirect" in driver.page_source
#     print("\033[32mCheck that store added correctly when click on it and click Back:: Passed\033[0m")

#     ##############  Check that store disappear when click on it and click back ##############
#     AddStore = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Add Store")
#     AddStore.click()

#     Store_Beddinginn = wait.until(EC.presence_of_element_located((By.XPATH,'//android.view.View[@content-desc="Beddinginn"]/android.view.View')))
#     Store_Beddinginn.click()
#     Done_Button = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Done")
#     Done_Button.click()

#     assert "Beddinginn" not in driver.page_source
#     print("\033[32mCheck that store disappear when click on it and click done:: Passed\033[0m")

#     ##############  Check that store disappear when click on it and click back ##############
#     AddStore = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Add Store")
#     AddStore.click()

#     Store_CruiseDirect = wait.until(EC.presence_of_element_located((By.XPATH,'//android.view.View[@content-desc="CruiseDirect"]/android.view.View')))
#     Store_CruiseDirect.click()
#     Back_Button = driver.find_element(MobileBy.CLASS_NAME, "android.widget.Button")
#     Back_Button.click()

#     assert "CruiseDirect" not in driver.page_source
#     print("\033[32mCheck that store disappear when click on it and click Back:: Passed\033[0m")

HomePage()