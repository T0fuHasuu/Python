""" **Tips**
To Have This work you need to have the correct version of ChromeDriver Stable and also Chrome itself
This is Version 128 both Chrome and ChromeDriver 

Required :
_ ChromDriver 128 : https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/win64/chromedriver-win64.zip
_ Chrome 
_ Selenium : pip install selenium (Terminal)
"""

import tensorflow as tf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import for Select
import subprocess
import time

# Define the Source
username = "66122420126"
password = "20062547"
url = "https://reg.ubru.ac.th/login.aspx"

# Check wifi state
def WifiState():
    result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True)
    
    if 'Wi-Fi' in result.stdout:
        print("WiFi is enabled")
    else:
        print("Enable WiFi first")

# Function to select the term
def select_term(driver):
    try:
        dropdown = Select(driver.find_element(By.ID, 'ddTerm'))  # Ensure Select is imported
        
        # Select the option with the visible text "3/2566"
        dropdown.select_by_visible_text("3/2566")
        
        print("Successfully selected '3/2566'.")
    except Exception as e:
        print(f"Error occurred while selecting '3/2566': {e}")

# Press the booking option
def booking_press(driver):
    try:
        reserv_link = driver.find_element(By.LINK_TEXT, "จองรายวิชา")
        reserv_link.click()
        print("Clicked on the 'จองรายวิชา' link successfully.")
    except Exception as e:
        print(f"Error occurred while trying to click on 'จองรายวิชา': {e}")

# Function to search by subject code
def search_by_subject_code(driver, subject_code):
    try:
        # Locate the subject code input field by its ID and enter the subject code
        subject_input = driver.find_element(By.ID, 'txtSubjCode')
        subject_input.send_keys(subject_code)
        
        # Locate and click the search button by its ID
        search_button = driver.find_element(By.ID, 'Button1')
        search_button.click()
        
        print(f"Successfully searched for subject code: {subject_code}")
    except Exception as e:
        print(f"Error occurred while searching for subject code: {e}")

# Section Picking
def press_link_by_href(driver, href_value):
    try:
        # Find the link element by its href attribute using XPath
        link_element = driver.find_element(By.XPATH, f"//a[@href='{href_value}']")
        link_element.click()
        print(f"Clicked on the link with href '{href_value}' successfully.")
    except Exception as e:
        print(f"Error occurred while trying to click on link with href '{href_value}': {e}")

# TensorFlow Lite Model Handling without XNNPACK
# def load_tflite_model(model_path):
#     try:
#         # Disable XNNPACK delegate
#         interpreter = tf.lite.Interpreter(model_path=model_path, experimental_delegates=[])
        
#         # Allocate tensors
#         interpreter.allocate_tensors()
        
#         print(f"Successfully loaded TFLite model from '{model_path}' without XNNPACK delegate.")
        
#         # Optionally, you can get input and output details
#         input_details = interpreter.get_input_details()
#         output_details = interpreter.get_output_details()
        
#         # Example usage of input and output handling
#         # interpreter.set_tensor(input_details[0]['index'], your_input_data)
#         # interpreter.invoke()
#         # output_data = interpreter.get_tensor(output_details[0]['index'])
        
#     except Exception as e:
#         print(f"Error occurred while loading TFLite model from '{model_path}': {e}")


# Login bot
def startBot(username, password, url):
    path = "C:\\Users\\yuutd\\projects\\ProgramData\\chromedriver-win64\\chromedriver.exe"
    service = Service(executable_path=path)
    
    driver = webdriver.Chrome(service=service)
    
    driver.get(url)
    
    driver.find_element(By.ID, "txtUser").send_keys(username)
    
    driver.find_element(By.ID, "txtPass").send_keys(password)
    
    driver.find_element(By.ID, "btLogin").click()
    
    # Perform actions on the page
    booking_press(driver)
    select_term(driver)
    search_by_subject_code(driver, "9032111")
    press_link_by_href(driver, "https://reg.ubru.ac.th/reservview.aspx?tbid=663903211100302&d=%E0%B8%AA%20&s=7.10%20&e=10.30&d2=%E0%B8%AD%E0%B8%B2&s2=7.10%20&e2=10.30&d3=-%20&s3=-%20%20%20%20&e3=-")

    
    # Load and handle the TensorFlow Lite model
    # load_tflite_model(model_path)
    
    while True:
        time.sleep(1) 

# Organize
def Ready_End():
    print("Starting Process")
    WifiState()
    startBot(username, password, url)
    print("Finished Connecting!")

# Starting Process
Ready_End()
