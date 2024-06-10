from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from Setup import setup
from appium.webdriver.common.appiumby import By as MobileBy

x = 300
y = 300

Search_data = ["XXX" , "amazon" , "mo" , "on the run" , "2b"]

def General_Search():
    driver, wait = setup()
    #, action = setup()
    LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
    LoginButton.click()

    Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
    Email.click()
    Email.clear()
    Email.send_keys("gnohair@gmail.com")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')

    time.sleep(1)
    Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Password.click()
    Password.clear()
    Password.send_keys("Uu777777")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done') #to hide the keyboard

    Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
    Login.click()

    time.sleep(2)
    #action.tap(x=x, y=y).perform() #to click on any position on screen

    time.sleep(3)
    SearchBox = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Type to Search')))
    SearchBox.click()

    print("\n\n" + "*"*50)
    print(" "*15 + " Search Test Cases " + " "*15)
    print("*"*50 +"\n")

    for item in Search_data:
        time.sleep(5)
       # Search = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText')))
        Search = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.EditText')))
        Search.click()
        Search.clear()
        Search.send_keys(item)

        if item == "XXX":
                try:
                    time.sleep(5)
                    assert "No Result Found" in driver.page_source
                    print("\033[32mCheck that sentence No Result Found appear when user insert wrong data in search field:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck that sentence No Result Found appear when user insert wrong data in search field:: Failed\033[0m")
        #########################################################
        elif item == "amazon":
                try:
                    time.sleep(5)
                    stores_section = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Stores')))
                    time.sleep(5)
                    Allpage = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View')))

                    Amazon_searsh_result = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'Amazon.eg Up to 7.00%')))
                    #Amazon_searsh_result = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Amazon.eg Up to 7.00%"]/android.view.View/android.widget.ImageView')
                    time.sleep(5)
                    print(Amazon_searsh_result.get_attribute("content-desc"))
                    if Amazon_searsh_result in driver.page_source:
                       print("\033[32mTest2 Passed\033[0m")
                    else:
                        print("\033[31mTest2 Failed\033[0m")
                # except Exception as e:
                #     print("\033[31mTest2 Failed\033[0m")
                except Exception as e:
                 print(f"\033[31mAmazon search test failed due to {str(e)}\033[0m")
                 driver.save_screenshot(f"error_{item}.png")  # Save a screenshot for debugging

        # elif item[0] == "mo":
        #         try:
        #             time.sleep(2)
        #             assert "Al Mokhtabar 3.00% cash back Was 2.50%" and "TFK Up to 6.00% Was 5.00%" in driver.page_source
        #             print("search test3 Passed")
        #         except Exception as e:
        #             print("search test3 Failed")
        
        # elif item[0] == "on the run":
        #         try:
        #             time.sleep(2)
        #             assert "Stores On the Run 3.00% cash back Was 2.50%" in driver.page_source
        #             print("search test4 Passed")
        #         except Exception as e:
        #             print("search test4 Failed")

        # elif item[0] == "2b":
        #         try:
        #             time.sleep(2)
        #             assert "Stores 2B Egypt 1.20% Was 1.00% 1.20% cash back Was 1.00%" in driver.page_source
        #             print("search test4 Passed")
        #         except Exception as e:
        #             print("search test4 Failed")

def AllStores():
    driver, wait = setup()
    #, action = setup()
    LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
    LoginButton.click()

    Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
    Email.click()
    Email.clear()
    Email.send_keys("gnohair@gmail.com")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')

    time.sleep(1)
    Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Password.click()
    Password.clear()
    Password.send_keys("Ng555555")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

    Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
    Login.click()

    time.sleep(2)
    #action.tap(x=x, y=y).perform() #to click on any position on screen

    menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Menu"]')))
    menu.click()

    AllStores = driver.find_element(MobileBy.ACCESSIBILITY_ID, "All Stores")
    AllStores.click()

    print("\n\n" + "*"*50)
    print(" "*15 + " General Search Test Cases " + " "*15)
    print("*"*50 +"\n")

General_Search()
# time.sleep(2)
# driver.quit()