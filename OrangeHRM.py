import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

###  DRAWBACKS ####

# parallel run
# reports
# Data driven
# hardcode value
# grouping \ selection test cases
# multiple time write same type of code
# time consuming