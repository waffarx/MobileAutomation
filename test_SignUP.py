from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time
#from appium.webdriver.common.touch_action import TouchAction
from Setup import setup
from appium.webdriver.common.appiumby import By as MobileBy

x = 300
y = 300

test_results = []
def get_random_email():
    domains = ["TestAutomation1.com", "TestAutomation2.com", "TestAutomation3.com"]
    letters = string.ascii_lowercase[:12]   # 12 random letters

    email = "".join(random.choice(letters) for i in range(7))  # 7 random letters
    email += "@"
    email += random.choice(domains)

    return email

Signup_data_withEmail= [
    ["@@@343443", get_random_email(), "Qw222222"],
    ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", get_random_email(), "Qw222222"],
    ["Ahmed", "Email@", "Qw222222"],
    ["Ahmed", "gnohair@gmail.com", "Qw222222"],
    ["Ahmed", "     gnohair@gmail.com    ", "Qw222222"],
    #["Ahmed", get_random_email() ,"123ee"],
    [" ", " ", " "],
    ["Yahia", get_random_email(), "Qw222222"],
]

Signup_data_withMobile= [
    ["Yahia", "01067802082", "Qw222222"],  #number already used
    ["Yahia", "01067802082222222", "Qw222222"],
    ["Yahia", "01277249225", "Qw222222"],
]

def test_Signup_withEmail():
    driver, wait = setup()
    #, action
    print("\n\n" + "*"*50)
    print(" "*10 + "SignUp with Email Test Cases" + " "*10)
    print("*"*50 +"\n")

    for item in Signup_data_withEmail:
        time.sleep(0.5)
        Name = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
        Name.click()
        Name.clear()
        Name.send_keys(item[0])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        Email = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
        Email.click()
        Email.clear()
        Email.send_keys(item[1])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        Password = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]')))
        Password.click()
        Password.clear()
        Password.send_keys(item[2])
        
        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')    # to hide the keyboard

        JoinNow = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Join Now')))
        JoinNow.click()
        
        time.sleep(0.5)
        ########################################### Name Test Cases ############################################
        if item[0] == "@@@343443":
                try:
                    assert "The name should contain letters only" in driver.page_source
                    print("\033[32mCheck system appear error message when insert numbers or symbols in Name:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert numbers or symbols in Name:: Failed\033[0m")

        elif item[0] == "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA":
                try:
                    assert "Doesn't exceed 50 character" in driver.page_source
                    print("\033[32mCheck system appear error message when insert more than 50 character in Name:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert more than 50 character in Name:: Failed\033[0m")
       
        ########################################### Email Test Cases ############################################
        elif item[1] == "Email@":
                try:
                    assert "Email should be like example@example.com" in driver.page_source
                    print("\033[32mCheck system appear error message when insert wrong format in mail:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert wrong format in mail:: Failed\033[0m")

        elif item[1] == "gnohair@gmail.com":
                try:
                    assert "This account already exists" in driver.page_source
                    print("\033[32mCheck system appear error message when insert mail already exists:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Ok"]')))
                    Ok_buttomSheet.click()
                    time.sleep(0.5)
                    driver.hide_keyboard(strategy='pressKey', key='Done')
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert mail already exists:: Failed\033[0m")

        elif item[1] == "     gnohair@gmail.com    ":
                try:
                    assert "This account already exists" in driver.page_source
                    print("\033[32mCheck system teminate spaces:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Ok"]')))
                    Ok_buttomSheet.click()
                    time.sleep(0.5)
                    driver.hide_keyboard(strategy='pressKey', key='Done')
                except Exception as e:
                    print("\033[31mCheck system teminate spaces:: Failed\033[0m")

        elif item[0] == " " and item[1] == " "and item[2] == " ": #if all fields are empty
                try:
                    assert "Please, enter your name" and "Please, enter your email or Mobile number" and "This field is required" in driver.page_source
                    print("\033[32mCheck system appear error message when click JoinNow without insert any data:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when click JoinNow without insert any data:: Failed\033[0m")
        
        ########################################### Correct signup Test Case ############################################
        elif item[0] == "Yahia" and item[2] == "Qw222222":
                try:
                    time.sleep(5)
                    #action.tap(x=x, y=y).perform()  #to click on any position on screen
                    time.sleep(5)
                    menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Menu"]')))
                    content_desc = menu.get_attribute('content-desc')
                    assert content_desc in driver.page_source  
                    print("\033[32mCheck SignUP work Successfully:: Passed\033[0m")
                except Exception as e:
                   print("\033[31mCheck SignUP work Successfully:: Failed\033[0m")

    driver.quit()

def test_signup_withMobile():
    driver, wait, = setup()
    #action 
    print("\n\n" + "*"*50)
    print(" "*15 + "SignUp with Mobile Test Cases" + " "*15)
    print("*"*50 +"\n")
    for item in Signup_data_withMobile:
        Name = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
        Name.click()
        Name.clear()
        Name.send_keys(item[0])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        Email = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
        Email.click()
        Email.clear()
        Email.send_keys(item[1])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        Password = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]')))
        Password.click()
        Password.clear()
        Password.send_keys(item[2])
        
        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

        RequestOTP = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Request OTP')))
        RequestOTP.click()
        
        time.sleep(0.5)
        if item[1] == "01067802082":
                try:
                    assert "This mobile number has already been registered." in driver.page_source
                    print("\033[32mCheck system appear error message when insert mobile number already registered:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Ok"]')))
                    Ok_buttomSheet.click()
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert mobile number already registered:: Failed\033[0m")
       
        elif item[1] == "01067802082222222":
                try:
                    assert "This mobile number is not valid" in driver.page_source
                    print("\033[32mCheck system appear error message when insert not valid mobile number:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert not valid mobile number:: Failed\033[0m")

        elif item[1] == "01277249225":
                try:
                    assert "A verification code was sent to this mobile number 01277249225" in driver.page_source
                    print("\033[32mCheck page of verification open when insert correct mobile number:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck page of verification open when insert correct mobile number:: Failed\033[0m")
    driver.quit()

test_Signup_withEmail()
#test_signup_withMobile()

#Logout = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Sign Out"]')))
#driver.execute_script("arguments[0].scrollIntoView(true);", Logout)