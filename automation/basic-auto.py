from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
import time

# setup browser options
options = webdriver.ChromeOptions()
options.headless = False  # true = runs browser in headless mode i.e invisible

# init the webdriver
WEBDRIVER_PATH = "D:\MyWorkspace\python-projects\chromedriver.exe"
driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)
# driver.maximize_window()  # maximize the window

driver.get("https://www.google.com")  # open an URL in the browser

source = driver.page_source  # get page source contents of the current page

elem1 = driver.find_element_by_id("searchform")  # find element by ID
print(elem1)

elem = driver.find_element_by_class_name("gNO89b")  # find element by ID
print(elem)

links = driver.find_elements_by_tag_name('a')  # find element by tag name
print(links)

# find by XPath i.e dialog elem. with class as spch-dlg
tag_list = driver.find_elements_by_xpath("//dialog[@class='spch-dlg']")
print(tag_list)

print(links[0].text)  # get element text
print(elem.parent)  # get elem. parent elem.

print(links[0].get_attribute("href"))  # get elem. attribute value

elem = driver.find_element_by_name("q")
elem.send_keys("Some text")  # press keys within elem.
elem.send_keys(Keys.CONTROL, 'a')

links[0].click()  # click an element

# driver.execute_script("script") # execute a scipt
driver.save_screenshot('screenshot.png')  # capture a screenshot

driver.add_cookie({'name': 'foo', 'value': 'bar'})
print(driver.get_cookies())

# driver to end of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# wait till element to be present
elem = driver_wait(driver, 10).until(
    ec.presence_of_element_located((by.XPATH, "//a[@title='Create an account']")))

time.sleep(3)  # delay of 3 seconds

driver.close()  # close the browser
