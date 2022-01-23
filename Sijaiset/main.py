from distutils.log import error
from tkinter import E
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


# Using Chrome to access web
driver = webdriver.Chrome()
# navigate to site
driver.get(os.getenv("URL"))

# Login
if driver.find_element(By.ID, "id_username"):
    id_user = driver.find_element(By.ID, "id_username")
    id_password = driver.find_element(By.ID, "id_password")
    login_btn = driver.find_element(By.CLASS_NAME, 'tyer-btn')
    # Send id information
    id_user.send_keys(os.getenv("USER_ID"))
    id_password.send_keys(os.getenv("USER_PASSWORD"))
    login_btn.click()


# change page
url = "?page=2"
change_page_btn = driver.find_element_by_xpath('//a[@href="'+url+'"]')
change_page_btn.click() 

# Loop days check if sunday
# Get the rows
rows = driver.find_elements_by_xpath("//table/tbody/tr")

# Iterate over the rows
dateFound = False
for row in rows:
    # Get all the columns for each row. 
    # cols = row.find_elements_by_xpath("./*")
    cols = row.find_elements_by_xpath("./*[name()='th' or name()='td']")
    temp = [] # Temporary list
    for col in cols:
        if dateFound == True:
            if "Tiedot" in col.text:
                temp.append(col)
                col.click()
                sleep(3)
        try:
            strTime = str(col.text)
            converted = datetime.strptime(strTime, '%d.%m.%Y')
            if converted.weekday() == 5:
                dateFound = True
                print("Found")
        except ValueError :
            continue
        
