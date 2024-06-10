from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.appiumby import By as MobileBy
#from appium.webdriver.common.touch_action import TouchAction
from Setup import setup

x = 300
y = 300

ForgetPassword_Email_Data= [
    [" "],
    ["Email@"],
    ["     gnohair@gmail.com    "],
    ["gnohair@testgmail.com"],
]

ForgetPassword_Mobile_Data= [
    [" "],
    ["01011111111"],
    ["01077778877877787878"],
  #  ["01067802082"],
]

def test_ForgetPassword_Email():
     driver, wait = setup()
     LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Log In')))
     LoginButton.click()

     ForgetPassword_Button = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Forget Password ?')))
     ForgetPassword_Button.click()

     BottomSheet_Email = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Reset Password via Email')))
     BottomSheet_Email.click()

     print("\n\n" + "*"*50)
     print(" "*10 + "ForgetPassword by Email Test Cases " + " "*15)
     print("*"*50 +"\n")

     for item in ForgetPassword_Email_Data:
        Email = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.EditText')))
        Email.click()
        Email.clear()
        Email.send_keys(item[0])

        SendEmail = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Send an email')))
        SendEmail.click()

        if item[0] == " ":
                try:
                    assert "Email should be like example@example.com" in driver.page_source
                    print("\033[32mCheck system appear error message when click send mail without insert any data:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when click send mail without insert any data:: Failed\033[0m")
        
        elif item[0] == "Email@":
                try:
                    assert "Email should be like example@example.com" in driver.page_source
                    print("\033[32mCheck system appear error message when insert wrong format in mail:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert wrong format in mail:: Failed\033[0m")
        
        elif item[0] == "     gnohair@gmail.com    ":
                try:
                    assert "An E-mail has been sent to your email." in driver.page_source
                    print("\033[32mCheck system teminate spaces:: Passed\033[0m")
                    time.sleep(1)
                    Continue_buttomSheet = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Continue')))
                    Continue_buttomSheet.click()
                    time.sleep(0.5)
                    driver.hide_keyboard(strategy='pressKey', key='Done')
                except Exception as e:
                    print("\033[31mCheck system terminate spaces:: Failed\033[0m")

        if item[0] == "gnohair@testgmail.com":
                try:
                    assert "The e-mail that you entered is wrong" in driver.page_source
                    print("\033[32mCheck error message appear when insert wrong email:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck error message appear when insert wrong email:: Failed\033[0m")
     driver.quit()

def test_ForgetPassword_Mobile():
     driver, wait = setup()
     #, action = setup()
     LoginButton = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Log In')))
     LoginButton.click()

     ForgetPassword_Button = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Forget Password ?')))
     ForgetPassword_Button.click()

     BottomSheet_Mobile = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Reset Password via Mobile')))
     BottomSheet_Mobile.click()

     print("\n\n" + "*"*50)
     print(" "*10 + "ForgetPassword by Mobile Test Cases " + " "*15)
     print("*"*50 +"\n")

     for item in ForgetPassword_Mobile_Data:
        PhoneNumber = wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.EditText')))
        PhoneNumber.click()
        PhoneNumber.clear()
        PhoneNumber.send_keys(item[0])

        RequestOTP = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Request OTP')))
        RequestOTP.click()

        if item[0] == " ":
                try:
                    assert "Please, enter your phone number." in driver.page_source
                    print("\033[32mCheck system appear error message when click send otp without insert any data:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when click send otp without insert any data:: Failed\033[0m")
        
        elif item[0] == "01011111111":
                try:
                    assert "This mobile number is not associated with a WaffarX account" in driver.page_source
                    time.sleep(5)
                    #action.tap(x=x, y=y).perform()
                    print("\033[32mCheck system appear error message when insert mobile number is not associated with a WaffarX account:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert mobile number is not associated with a WaffarX account:: Failed\033[0m")
        
        elif item[0] == "01077778877877787878":
                try:
                    assert "Your phone number must be 11 numbers" in driver.page_source
                    print("\033[32mCheck system appear error message when insert not valid mobile number:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck system appear error message when insert not valid mobile number:: Failed\033[0m")

        elif item[0] == "01067802082":
                try:
                    assert "Forget password code sent to this mobile number 01067802082" in driver.page_source
                    print("\033[32mCheck page of insert otp open when insert correct mobile number:: Passed\033[0m")
                except Exception as e:
                    print("\033[31mCheck page of insert otp open when insert correct mobile number:: Failed\033[0m")
     driver.quit()

#test_ForgetPassword_Email()
test_ForgetPassword_Mobile()