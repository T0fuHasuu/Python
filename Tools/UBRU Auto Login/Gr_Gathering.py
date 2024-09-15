from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json
import pandas as pd

# Load users from a JSON file
with open('std2566.json', 'r') as f:
    data = json.load(f)
    users = data['users']

url = "https://reg.ubru.ac.th/login.aspx"
path = "C:\\Users\\yuutd\\projects\\ProgramData\\chromedriver-win64\\chromedriver.exe"

# Function to get subject names, sections, and grades for a user
def get_subjects_sections_and_grades(driver):
    index = 2  # Starting index (for dgv_ctl02_lblgrade, dgv_ctl02_lblsubjname, dgv_ctl02_lblsection)
    subjects_data = []  # Store subject_name : section : grade pairs
    
    while True:
        # Construct the dynamic IDs for subject name, grade, and section
        subject_id = f"dgv_ctl{index:02}_lblsubjname"
        grade_id = f"dgv_ctl{index:02}_lblgrade"
        section_id = f"dgv_ctl{index:02}_lblsection"
        
        try:
            # Try to find the elements by their IDs and extract the text
            subject_element = driver.find_element(By.ID, subject_id)
            grade_element = driver.find_element(By.ID, grade_id)
            section_element = driver.find_element(By.ID, section_id)
            
            subject_name = subject_element.text
            grade_text = grade_element.text
            section_text = section_element.text
            
            # Store the subject_name : section : grade pair
            subjects_data.append(f"{subject_name} (Sec: {section_text}) : {grade_text}")
            print(f"{subject_name} (Section: {section_text}) : {grade_text}")
            
            # Increment the index for the next element
            index += 1
        except NoSuchElementException:
            # If the element is not found, break the loop
            print(f"No more elements found after index {index}. Stopping.")
            break
            
    return subjects_data

# Convert to xlsx file
def ConvertDoc():
    # Step 1: Load the JSON data from the file
    with open('user_results.json', encoding='utf-8') as json_file:
        user_results = json.load(json_file)  # Corrected here

    # Step 2: Process the JSON data to extract name, ID, subjects, and grades
    results = []
    for student in user_results:
        student_info = {
            "Name": student["name"],
            "ID": student["username"]
        }
        for subject_data in student["subjects_data"]:
            subject, grade = subject_data.split(" : ")
            student_info[subject] = grade
        results.append(student_info)
    
    # Step 3: Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(results)
    
    # Step 4: Fill NaN values with an empty string (optional)
    df.fillna('', inplace=True)
    
    # Step 5: Save the DataFrame to an Excel file
    df.to_excel('Result.xlsx', index=False)


# List to store results for all users
all_user_results = []

# Iterate over each user in the users array
for user in users:
    # Initialize WebDriver for each user
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    
    # Open the login page
    driver.get(url)
    
    # Log in with the current user's credentials
    driver.find_element(By.ID, "txtUser").send_keys(user["username"])
    driver.find_element(By.ID, "txtPass").send_keys(user["password"])
    driver.find_element(By.ID, "btLogin").click()

    # Get user's name
    try:
        user_name_element = driver.find_element(By.ID, "Top3_Label2")
        user_name = user_name_element.text
    except NoSuchElementException:
        user_name = "Name not found"
    
    # result_tab
    reserv_link = driver.find_element(By.LINK_TEXT, "ตรวจสอบผลการเรียน")
    reserv_link.click()
    print(f"Clicked on the 'ตรวจสอบผลการเรียน' link successfully for user {user['username']}.")

    time.sleep(1)

    # Get subjects, sections, and grades for the current user
    subjects_data = get_subjects_sections_and_grades(driver)
    
    # Store the results in the list
    user_result = {
        "name": user_name,
        "username": user["username"],
        "subjects_data": subjects_data
    }
    all_user_results.append(user_result)
    
    print(f"All extracted subject names, sections, and grades for user {user['username']}: {subjects_data}")

    # End the process for the current user
    driver.quit()
    print(f"Process completed for user {user['username']}\n")

# Write the results to a JSON file
with open('user_results.json', 'w', encoding='utf-8') as f:
    json.dump(all_user_results, f, ensure_ascii=False, indent=4)

ConvertDoc()