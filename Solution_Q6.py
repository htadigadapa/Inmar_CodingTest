from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.inmar.com/")
print("Title of the page:\n"+driver.title)
driver.close()
