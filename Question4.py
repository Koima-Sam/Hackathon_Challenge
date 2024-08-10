# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:17:29 2024

@author: sam17
"""
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.google.com/")

#Get the search input
search = driver.find_element(By.ID, 'APjFqb')
driver.execute_script("arguments[0].click();", search)
search.clear()
search.send_keys("Test Automation") 

 #find the submit button of the search bar.
submitBtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
driver.execute_script("arguments[0].click();", submitBtn)


time.sleep(3)
# Check if Test Automation is there
search_data = driver.page_source
soup = BeautifulSoup(search_data, 'lxml')

if "Test Automation" in soup.text:
    print(soup.text)
    print("Test Automation was found.")
else:
    print("Test Automation not found.")

