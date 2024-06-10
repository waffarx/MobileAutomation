from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import By as MobileBy
from selenium.webdriver.support import expected_conditions as EC
import time
from Setup import setup

x = 300
y = 300

def AllStores():
    driver, wait, action = setup()
    LoginButton = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Log In"]')))
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

    Login = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Log In"]')))
    Login.click()
    time.sleep(0.5)

    # time.sleep(4)
    # action.tap(x=x, y=y).perform()  # to click on any position on screen

    Menu = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Menu')))
    Menu.click()

    print("\n\n" + "*"*50)
    print(" "*10 + " AllStores Test Cases " + " "*15)
    print("*"*50 +"\n")

    AllStores_choice = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="All Stores"]')))
    AllStores_choice.click()

    time.sleep(2)
    AllStores_List = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')))

    ListItems = AllStores_List.find_elements(By.CLASS_NAME, "android.view.View")
    print(f"Number of items found: {len(ListItems)}")

    # Iterate over the list items and perform actions
    for item in ListItems:
        content_desc = (item.get_attribute('content-desc'))
        print(content_desc)

    driver.quit()

def AmazonGiftCard():
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

    time.sleep(2)
    Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Password.click()
    Password.clear()
    Password.send_keys("Ng555555")
        
    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

    Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
    Login.click()
    time.sleep(0.5)

    #time.sleep(4)
    #action.tap(x=x, y=y).perform()  # to click on any position on screen

    Menu = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Menu')))
    Menu.click()

    print("\n\n" + "*"*50)
    print(" "*10 + " Amazon Gift Card Test Cases " + " "*15)
    print("*"*50 +"\n")

    Cashback_on_giftcard_Choice = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Cashback on Gift Card')))
    Cashback_on_giftcard_Choice.click()

    Purchase_GiftCard_Choice = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Purchase Gift Card')))
    Purchase_GiftCard_Choice.click()

    time.sleep(2)

    Amazon_GiftCard = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.ImageView')))
    Amazon_GiftCard.click()

    # time.sleep(2)
    # Write_number = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.EditText[@text="10"]')))
    # Write_number.click()
    # Write_number.clear()
    # Write_number.send_keys("0")

    # Error = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'The amount must be between 1 and 6000 Quick Purchase')))
    # assert Error in driver.page_source
    # print("ok")

    # Quick_Purchase = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Quick_Purchase')))

    Choice_100EGP = wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.view.View[@content-desc="EGP 100"]')))
    Choice_100EGP.click()

    assert "Order Subtotal 100 Service fees 0.0 Total Amount 100.0" in driver.page_source
    print("\033[32mCheck that data of subtotal and other data correct when click on fixed numbers:: Passed\033[0m")

AmazonGiftCard()