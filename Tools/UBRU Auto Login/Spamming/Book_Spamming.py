""" 
**Tips**
To Have This work you need to have the correct version of ChromeDriver Stable and also Chrome itself
This is Version 128 both Chrome and ChromeDriver 

Required :
_ ChromDriver 128 : https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/win64/chromedriver-win64.zip
_ Chrome 
_ Selenium : pip install selenium (Terminal)
_ tensorflow : pip install tensorflow (Terminal) 
"""

# Import 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time
import json

# Define the Source
json_file_path = 'Info.json'  

# Load credentials from JSON file
with open(json_file_path, 'r') as file:
    credentials = json.load(file)
    username = credentials.get('username')
    password = credentials.get('password')
    term = credentials.get('term') 
    subject_code = credentials.get('subject_code') 
    href_value = credentials.get('href_value')
    
url = "https://reg.ubru.ac.th/login.aspx"

# Check wifi state
def WifiState():
    result = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True, text=True)
    if 'Wi-Fi' in result.stdout:
        print("WiFi is enabled")
    else:
        print("Enable WiFi first")

# booking Button
def booking_press(driver):
    try:
        reserv_link = driver.find_element(By.LINK_TEXT, "จองรายวิชา")
        reserv_link.click()
        print("Clicked on the 'จองรายวิชา' link successfully.")
    except Exception as e:
        print(f"Error occurred while trying to click on 'จองรายวิชา': {e}")
        
# Select Term
def select_term(driver):
    try:
        dropdown = Select(driver.find_element(By.ID, 'ddTerm')) 
        dropdown.select_by_visible_text(term) 
        print(f"Successfully selected '{term}'.")
    except Exception as e:
        print(f"Error occurred while selecting '{term}': {e}")

# Subject code
def code_sub(driver, subject_code):
    try:
        # code
        subject_input = driver.find_element(By.ID, 'txtSubjCode')
        subject_input.send_keys(subject_code) 
        # button search
        search_button = driver.find_element(By.ID, 'Button1')
        search_button.click()
        print(f"Successfully searched for subject code: {subject_code}")
    except Exception as e:
        print(f"Error occurred while searching for subject code: {e}")

# Section Picking
def press_link(driver, href_value):
    try:
        driver.get(href_value)
        print(f"Successfully navigated to the link with href '{href_value}'.")
    except Exception as e:
        print(f"Error occurred while trying to navigate to link with href '{href_value}': {e}")

# Confirm
def confirm_bt(driver):
    try:
        save_button = driver.find_element(By.ID, 'btSave')
        save_button.click()
        print("Clicked the 'btSave' button successfully.")
        
        # Wait for the alert to be present and accept it
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.accept()
        print("Alert accepted.")
    except Exception as e:
        print(f"Error occurred while trying to click on 'btSave' or handle alert: {e}")

# Login bot
def startBot(username, password, url):
    path = "C:\\Users\\yuutd\\projects\\ProgramData\\chromedriver-win64\\chromedriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.find_element(By.ID, "txtUser").send_keys(username)
    driver.find_element(By.ID, "txtPass").send_keys(password)
    driver.find_element(By.ID, "btLogin").click()
    
    # wait 1s
    time.sleep(1)
    
    # Perform actions on the page
    booking_press(driver)
    select_term(driver)
    code_sub(driver, subject_code) 
    press_link(driver, href_value)
    confirm_bt(driver)

    # Keep it open
    while True:
        time.sleep(1) 

# Organize
def Ready_End():
    print("Starting Process")
    WifiState()
    startBot(username, password, url)
    print("Finished !")

# Starting Process
Ready_End()
