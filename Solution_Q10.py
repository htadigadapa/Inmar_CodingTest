import time
import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver = webdriver.Firefox()
driver.get("http://www.seleniumframework.com/Practiceform/ ")
driver.find_element_by_xpath("//*[@onclick='newBrwTab()']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
print("New tab title : "+ driver.title)
driver.switch_to.window(driver.window_handles[0])
print("Main tab title : "+ driver.title)
print("Total tabs opened : "+ str(len(driver.window_handles)))
