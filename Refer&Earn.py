from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import By as MobileBy
from selenium.webdriver.support import expected_conditions as EC
import time
from Setup import setup

x = 300
y = 300

Refer_data = [
    [" "],
    ["Email@"],
    ["   gnohair@gmail.com  "],
    ["lobna.mostafa95@gmail.com"],
   # ["j23134263@gmail.com"],
]

def Refer():
    driver, wait= setup()
    #, action 
    LoginButton = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Log In"]')))
    LoginButton.click()

    Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
    Email.click()
    Email.clear()
    Email.send_keys("gnohair@gmail.com")

    driver.hide_keyboard(strategy='pressKey', key='Done')

    time.sleep(2)
    Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Password.click()
    Password.clear()
    Password.send_keys("Ng555555")
        
    driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

    Login = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Log In"]')))
    Login.click()
    
    # time.sleep(4)
    # action.tap(x=x, y=y).perform()  # to click on any position on screen

    Menu = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Menu')))
    Menu.click()

    print("\n\n" + "*"*50)
    print(" "*10 + " Refer&Earn Test Cases " + " "*15)
    print("*"*50 +"\n")

    MyAccount_List = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="My Account"]')))
    MyAccount_List.click()

    Refer_and_Earn = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Refer and Earn')))
    Refer_and_Earn.click()

    for item in Refer_data:
        Email = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'android.widget.EditText')))
        Email.click()
        Email.clear()
        Email.send_keys(item[0])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        Button_send_Invitation = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Send Invitation')))
        Button_send_Invitation.click()

        # if item[0] == " ":
        #         try:
        #             assert "Email should be like example@example.com" in driver.page_source
        #             print("\033[32mCheck system appear error message when click send without insert data:: Passed\033[0m")
        #         except Exception as e:
        #             print("\033[31mCheck system appear error message when click send without insert data:: Failed\033[0m")

        if item[0] == "Email@":
                try:
                    assert "Email should be like example@example.com" in driver.page_source
                    print("\033[32mCheck system appear error message when insert wrong format in mail:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert wrong format in mail:: Failed\033[0m")

        # if item[0] == "   gnohair@gmail.com  ":
        #         try:
        #             time.sleep(3)
        #             assert "You cannot refer yourself. " in driver.page_source
        #             print("\033[32mCheck system appear error message when insert mail logged in:: Passed\033[0m")
        #             time.sleep(1)
        #             Ok_buttomSheet = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Ok')))
        #             Ok_buttomSheet.click()
        #         except Exception as e:
        #             print("\033[31mCheck system appear error message when insert mail logged in:: Failed\033[0m") 

        elif item[0] == "lobna.mostafa95@gmail.com":
                try:
                    time.sleep(1)
                    assert "This email is already registered." in driver.page_source
                    print("\033[32mCheck system appear error message when insert mail already registered:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Ok')))
                    Ok_buttomSheet.click()
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert mail already registered:: Failed\033[0m") 

        # elif item[0] == "j23134263@gmail.com":
        #         try:
        #             assert "This email is already registered." in driver.page_source
        #             print("\033[32mCheck system appear error message when insert mail already registered:: Passed\033[0m")
        #         except Exception as e:
        #             print("\033[31mCheck system appear error message when insert mail already registered.:: Failed\033[0m")
    
Refer()