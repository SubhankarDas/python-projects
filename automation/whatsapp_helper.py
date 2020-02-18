from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as driver_wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys
import time

WAIT_TIMEOUT = 1000

WEBDRIVER_PATH = "chromedriver.exe"
driver = webdriver.Chrome(WEBDRIVER_PATH)


def open_url(url):
    driver.get(url)


def search_chat(chat_username):
    chat_search_input = driver_wait(driver, WAIT_TIMEOUT).until(
        ec.presence_of_element_located((by.XPATH, "//input[@title='Search or start new chat']")))

    chat_search_input.send_keys(chat_username)


def select_chat(chat_username):
    chat_username_elem = driver_wait(driver, WAIT_TIMEOUT).until(
        ec.element_to_be_clickable((by.XPATH, "//span[@title='"+chat_username+"']")))

    chat_username_elem.click()


def send_message(message):
    chat_msg = driver_wait(driver, WAIT_TIMEOUT).until(
        ec.presence_of_element_located((by.XPATH, "//div[@contenteditable='true']")))
    chat_msg.send_keys(message)

    chat_msg.send_keys(Keys.ENTER)


def new_chat():
    new_chat_btn = driver_wait(driver, WAIT_TIMEOUT).until(
        ec.element_to_be_clickable((by.XPATH, "//div[@title='New chat']")))

    new_chat_btn.click()


def search_contact(name):
    contact_search_input = driver_wait(driver, WAIT_TIMEOUT).until(
        ec.presence_of_element_located((by.XPATH, "//input[@title='Search contacts']")))

    contact_search_input.send_keys(name)


def close_browser():
    time.sleep(10)
    driver.close()
