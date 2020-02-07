from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys

wait_timeout = 30


WEBDRIVER_PATH = "chromedriver.exe"
driver = webdriver.Chrome(WEBDRIVER_PATH)

driver.get("https://web.whatsapp.com")

chat_username = "Bhai"

# ---------------------------------------------
chat_search_input = driver_wait(driver, wait_timeout).until(
    ec.presence_of_element_located((by.XPATH, "//input[@title='Search or start new chat']")))

chat_search_input.send_keys(chat_username)

# ---------------------------------------------
'''
driver.find_element_by_xpath("//div[contains(text(),'Add User')]")
'''
chat_username_elem = driver_wait(driver, wait_timeout).until(
    ec.presence_of_element_located((by.XPATH, "//span[@title='"+chat_username+"']")))
print(chat_username_elem)

chat_username_elem.click()

# ---------------------------------------------
chat_msg = driver_wait(driver, wait_timeout).until(
    ec.presence_of_element_located((by.XPATH, "//div[@contenteditable='true']")))
chat_msg.send_keys('Hi from bot! Testing..')

chat_msg.send_keys(Keys.ENTER)
