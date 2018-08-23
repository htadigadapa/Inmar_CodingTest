from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.inmar.com ")
elements = driver.find_elements_by_tag_name('a')
for elem in elements:
    print(elem.get_attribute("href"))
    
driver.close()
