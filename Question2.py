# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:58:07 2024

@author: sam17
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

#get the url of the login page
driver.get("Login Url")
time.sleep(3)

#Get the username input, clear and input username
username = driver.find_element(By.ID, 'username')
driver.execute_script("arguments[0].click();", username)
username.clear()
username.send_keys('testuser') 

#Get the password input, clear and send the values
password = driver.find_element(By.ID, 'password')
driver.execute_script("arguments[0].click();", password)
password.clear()
password.send_keys('pass112') 

 #Submit the user.
loginBtn = driver.find_element(By.ID, 'loginBtn')
driver.execute_script("arguments[0].click();", loginBtn)

#check if welcome message is displayed
time.sleep(10)
welcome_message = driver.find_element(By.ID, 'welcome_message')
if welcome_message:
    print('logged in sucessfully')
else:
    print('Failed to login')

