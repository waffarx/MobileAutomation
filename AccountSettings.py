from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from appium.webdriver.common.touch_action import TouchAction

import time
from Setup import setup
import random
import string

x = 300
y = 300

def get_random_email():
    domains = ["TestAutomation1.com", "TestAutomation2.com", "TestAutomation3.com", "TestAutomation4.com" , "TestAutomation5.com", "TestAutomation6.com"]
    letters = string.ascii_lowercase[:12]   # 12 random letters

    email = "".join(random.choice(letters) for i in range(7))  # 7 random letters
    email += "@"
    email += random.choice(domains)

    return email

AccountSettings_data = [
    ["@#$222"],
    [" "],
    ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"],
    ["Nohair"],
    ["Nohair gamal omran"],
]

def AccountSettings():
    driver, wait, action = setup()
    print("\n\n" + "*"*50)
    print(" "*15 + " Account settings Test Cases " + " "*15)
    print("*"*50 +"\n")

    Name = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
    Name.click()
    Name.clear()
    Name.send_keys("AccountTest")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')

    time.sleep(1)
    Email = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Email.click()
    Email.clear()
    Email.send_keys(get_random_email())

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done') # to hide the keyboard

    Password = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]')))
    Password.click()
    Password.clear()
    Password.send_keys("Qw222222")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')    # to hide the keyboard

    JoinNow = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Join Now"]')))
    JoinNow.click()

    time.sleep(4)
    #action.tap(x=x, y=y).perform()  # to click on any position on screen

    menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Menu"]')))
    menu.click()

    MyAccount_List = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="My Account"]')))
    MyAccount_List.click()

    Accountsettings = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Account Settings"]')))
    Accountsettings.click()
    time.sleep(3)
    ############################## test ###########################
    FirstName = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@text="AccountTest"]')))
    FirstName.click()
    FirstName.clear()
    FirstName.send_keys(AccountSettings_data[0][0])

    # driver.hide_keyboard(strategy='pressKey', key='Done')

    # save = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc=" Save "]')))
    # save.click()
    # time.sleep(0.5)
   

#         # if item[0] == "@#$222" and item[1] == "@#$222":
#         #         try:
#         #             Error = wait.until(EC.presence_of_element_located((By.XPATH, '(//android.view.View[@content-desc="The name should contain letters only with no spaces"])[1]')))
#         #             if Error:
#         #                 print("\033[32mCheck system appear error message when insert numbers or symbols in Name:: Passed\033[0m")
#         #             # assert Error in driver.page_source
#         #             print("\033[32mCheck system appear error message when insert numbers or symbols in Name:: Passed\033[0m")
#         #         except Exception as e:
#         #             print("\033[31mCheck system appear error message when insert numbers or symbols in Name:: Failed\033[0m")

#         # elif item[0] == " " and item[1] == " ":
#         #         try:
#         #             assert "The name should contain letters only with no spaces" in driver.page_source
#         #             print("\033[32mCheck system appear error message when click save without insert firstname:: Passed\033[0m")
#         #         except Exception as e:
#         #             print("\033[31mCheck system appear error message when click save without insert firstname:: Failed\033[0m")

#         # elif item[0] == "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" and item[1] == "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA":
#         #         try:
#         #             assert "The name maximum length is 50 character" in driver.page_source
#         #             print("\033[32mCheck system appear error message when insert more than 50 character in Name:: Passed\033[0m")
#         #         except Exception as e:
#         #             print("\033[31mCheck system appear error message when insert more than 50 character in Name:: Failed\033[0m")

#         # elif item[0] == "Nohair" and item[1] == "Gamal":
#         #         try:
#         #             assert "Your account has been updated!" in driver.page_source
#         #             print("\033[32mCheck update data work Successfully:: Passed\033[0m")
#         #         except Exception as e:
#         #             print("\033[31mCheck update data work Successfully:: Failed\033[0m")
#         # count = count+1

#     driver.quit()
# AccountSettings()

def setup_account(driver, wait):
    print("\n\n" + "*" * 50)
    print(" " * 15 + "Account settings Test Cases" + " " * 15)
    print("*" * 50 + "\n")
    
    # Create a new account
    Name = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
    Name.click()
    Name.clear()
    Name.send_keys("AccountTest")
    print("Entered initial First Name: AccountTest")

    # Update the XPath expression to reflect the new first name
    FirstName_xpath = f'//android.widget.EditText[@text="AccountTest"]'

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')

    Email = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
    Email.click()
    Email.clear()
    Email.send_keys(get_random_email())
    print("Entered random email")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')  # to hide the keyboard

    Password = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]')))
    Password.click()
    Password.clear()
    Password.send_keys("Qw222222")
    print("Entered password")

    time.sleep(1)
    driver.hide_keyboard(strategy='pressKey', key='Done')  # to hide the keyboard

    JoinNow = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Join Now"]')))
    JoinNow.click()
    print("Clicked 'Join Now' button")

    time.sleep(4)
    # You can adjust the x and y coordinates according to your use case
    #action = TouchAction(driver)
    #action.tap(x=300, y=300).perform()  # Tap on a position on the screen (x=300, y=300 as an example)
    
    # Navigate to Account Settings
    menu = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Menu"]')))
    menu.click()
    print("Clicked Menu button")

    MyAccount_List = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="My Account"]')))
    MyAccount_List.click()
    print("Clicked My Account list")

    Accountsettings = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Account Settings"]')))
    Accountsettings.click()
    print("Clicked Account Settings")

    time.sleep(3)

    # Return the driver, wait, and the updated XPath expression for First Name
    return driver, wait, FirstName_xpath

# Function to process AccountSettings_data
def process_account_settings(driver, wait, first_name_xpath):
    # Define data sets
    AccountSettings_data = [
        ["@#$222" , "@#$222"],
        [" " , " "],
        ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" , "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"],
        ["Nohair" , "Gamal"],
    ]
    
    count = 0
    
    # Iterate through the data set
    for item in AccountSettings_data:
        FirstName_value = item[0]
        LastName_value = item[1]
        # Dynamically generate XPaths for First Name and Last Name
        if count == 0:
            
            Lastname_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View[2]/android.widget.ImageView[2]'
            Firstname_xpath = f'//android.widget.EditText[@text="AccountTest"]'
            
        else:
           Firstname_xpath = f'//android.widget.EditText[@text="{FirstName_value}"]'
           Lastname_xpath = f'//android.widget.EditText[@text="{LastName_value}"] '

        print(f"\nIteration {count + 1} - Processing First Name: {FirstName_value} and Last Name: {LastName_value}")

        # Interact with First Name field
        try:
            FirstName = wait.until(EC.presence_of_element_located((By.XPATH, Firstname_xpath)))
            FirstName.click()
            FirstName.clear()
            FirstName.send_keys(FirstName_value)
            driver.hide_keyboard(strategy='pressKey', key='Done')
            print(f"Entered First Name: {FirstName_value}")
        except Exception as e:
            print(f"Error interacting with First Name field: {e}")
            continue  # Skip to the next iteration on error

        # Interact with Last Name field
        try:
            LastName = wait.until(EC.presence_of_element_located((By.XPATH, Lastname_xpath)))
            LastName.click()
            LastName.clear()
            LastName.send_keys(LastName_value)
            driver.hide_keyboard(strategy='pressKey', key='Done')
            print(f"Entered Last Name: {LastName_value}")
        except Exception as e:
            print(f"Error interacting with Last Name field: {e}")
            continue  # Skip to the next iteration on error
        
        # Save changes
        try:
            save_button = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Save"]')))
            save_button.click()
            print("Changes saved successfully.")
        except Exception as e:
            print(f"Error clicking save button: {e}")
        
        # Update the First Name XPath after saving changes
        Firstname_xpath = f'//android.widget.EditText[@text="{FirstName_value}"]'
        
        # Increment the count
        count += 1

# Function to run AccountSettings tests
def AccountSettings():
    # Perform initial setup
    driver, wait , action= setup()
    
    # Perform initial account creation and setup
    driver, wait, first_name_xpath = setup_account(driver, wait)

    # Process account settings data
    process_account_settings(driver, wait, first_name_xpath)
    
    # Close the driver
    driver.quit()

# Run the AccountSettings function
AccountSettings()