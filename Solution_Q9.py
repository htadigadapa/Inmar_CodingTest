from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/practice-form.html")
driver.find_element_by_name("firstname").send_keys("Harsha")
driver.find_element_by_name("lastname").send_keys("Tadigadapa")

driver.find_element_by_id("sex-1").click()
driver.find_element_by_id("exp-4").click()
driver.find_element_by_id("datepicker").send_keys("NA")
driver.find_element_by_id("tea1").click()
driver.find_element_by_id("tool-1").click()
continent_dd = Select(driver.find_element_by_id("continents"))
continent_dd.select_by_index(2)

Select(driver.find_element_by_id("selenium_commands")).select_by_visible_text("Navigation Commands")
driver.find_element_by_id("submit").click()
try:
    assert(str(driver.title)=="Welcome")
    print("Home page opened")
except AssertionError:
    print("Home page not opened")
driver.close()
