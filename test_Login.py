from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import By as MobileBy
from selenium.webdriver.support import expected_conditions as EC
import time
from Setup import setup

x = 300
y = 300

Login_data_withEmail = [
    ["Email@", "Qw222222"],
    ["gnohair@gmail.com", "Qw222222"], # Correct Email and wrong Password
    ["     gnohair@gmail.com    ", "Qw222222"], # Correct Email and wrong Password
    [" ", " "],
    ["gnohair@gmail.commmmm", "Uu777777"], # Wrong Email and correct Password
    ["gnohair@gmail.com", "Uu777777"], #correct account
]

Login_data_withMobile= [
    ["01067802082", "Qw222222"],  #number already used
    ["01067802082222222", "Qw222222"],
]

def test_Login_withEmail():
   # driver, wait, action = setup()
    driver, wait = setup()
    LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
    LoginButton.click()
    print("\n\n" + "*"*50)
    print(" "*15 + "Login with Email Test Cases " + " "*15)
    print("*"*50 +"\n")

    for item in Login_data_withEmail:
        Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
        Email.click()
        Email.clear()
        Email.send_keys(item[0])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        time.sleep(2)
        Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
        Password.click()
        Password.clear()
        Password.send_keys(item[1])
        
        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

        Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
        Login.click()
        time.sleep(0.5)

        if item[0] == "Email@":
                try:
                    assert "Email should be like example@example.com" in driver.page_source
                    print("\033[32mCheck system appear error message when insert wrong format in mail:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert wrong format in mail:: Failed\033[0m")

        elif item[0] == "gnohair@gmail.com" and item[1] =="Qw222222":
                try:
                    assert "Incorrect username or password!" in driver.page_source
                    print("\033[32mCheck system appear error message when insert correct Email & wrong Password:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Ok"]')))
                    Ok_buttomSheet.click()
                    time.sleep(0.5)
                   # driver.hide_keyboard(strategy='pressKey', key='Done')
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert correct Email & wrong Password:: Failed\033[0m")

        elif item[0] == "     gnohair@gmail.com    ":
                try:
                    assert "Incorrect username or password!" in driver.page_source
                    print("\033[32mCheck system teminate spaces:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Ok"]')))
                    Ok_buttomSheet.click()
                    time.sleep(0.5)
                   # driver.hide_keyboard(strategy='pressKey', key='Done')
                except Exception as e:
                    print("\033[31mCheck system teminate spaces:: Failed\033[0m")

        elif item[0] == " " and item[1] == " ": #if all fields are empty
                try:
                    assert "Please, enter your email" in driver.page_source
                    print("\033[32mCheck system appear error message when click login without insert any data:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when click login without insert any data:: Failed\033[0m")

        elif item[0] == "gnohair@gmail.commmmm":
                try:
                    assert "Incorrect username or password!" in driver.page_source
                    print("\033[32mCheck system appear error message when insert wrong Email and correct Password:: Passed\033[0m")
                    time.sleep(1)
                    Ok_buttomSheet = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Ok"]')))
                    Ok_buttomSheet.click()
                    time.sleep(0.5)
                    driver.hide_keyboard(strategy='pressKey', key='Done')
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert wrong Email and correct Password:: Failed\033[0m")

        elif item[0] == "gnohair@gmail.com" and item[1] == "Uu777777":
                try:
                   time.sleep(5)
                   #action.tap(x=x, y=y).perform()  #to click on any position on screen
                   menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Menu"]')))
                   content_desc = menu.get_attribute('content-desc')
                   assert content_desc in driver.page_source  
                   print("\033[32mCheck Login work Successfully:: Passed\033[0m")
                except Exception as e:
                   print("\033[31mCheck Login work Successfully:: Failed\033[0m")
    driver.quit()

def test_Login_withMobile():
   # driver, wait, action = setup()
    driver, wait = setup()
    LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
    LoginButton.click()
    print("\n\n" + "*"*50)
    print(" "*15 + "Login with Mobile Test Cases " + " "*15)
    print("*"*50 +"\n")

    for item in Login_data_withMobile:
        Mobilenumber = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
        Mobilenumber.click()
        Mobilenumber.clear()
        Mobilenumber.send_keys(item[0])

        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done')

        time.sleep(2)
        Password = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
        Password.click()
        Password.clear()
        Password.send_keys(item[1])
        
        time.sleep(1)
        driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

        Login = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Log In")
        Login.click()
        time.sleep(0.5)

        if item[0] == "01067802082":
                try:
                    assert "You're unable to sign in with your mobile number. Try using another method." in driver.page_source
                    OK_Button = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Ok')))
                    OK_Button.click()
                    print("\033[32mCheck system appear error message when insert number which verified to account and not signup with it:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert number which verified to account and not signup with it:: Failed\033[0m")
                    
        elif item[0] == "01067802082222222":
                try:
                    assert "This mobile number is not valid" in driver.page_source
                    print("\033[32mCheck system appear error message when insert not valid mobile number:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert not valid mobile number:: Failed\033[0m")
                    
    driver.quit()
test_Login_withEmail()
#test_Login_withMobile()

# Google_Button = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Continue with Google"]')))
    # Google_Button.click()
    # driver.switch_to.window()