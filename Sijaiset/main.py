from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Using Chrome to access web
driver = webdriver.Chrome()
# navigate to site
driver.get(os.getenv("URL"))


if driver.find_element(By.ID,"id_username"):
    id_user = driver.find_element(By.ID,"id_username")
    id_password = driver.find_element(By.ID,"id_password")
    login_btn = driver.find_element(By.CLASS_NAME,'tyer-btn')
    # Send id information
    id_user.send_keys(os.getenv("USER_ID"))
    id_password.send_keys(os.getenv("USER_PASSWORD"))
    login_btn.click()


sleep(5)
