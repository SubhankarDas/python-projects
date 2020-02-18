import whatsapp_helper as wh
import time

USER_NAME = "Bhai"

wh.open_url("https://web.whatsapp.com")


def new_chat():
    wh.new_chat()
    wh.search_contact(USER_NAME)
    time.sleep(2)
    wh.select_chat(USER_NAME)
    wh.send_message("You are hacked!")


def recent_chat():
    wh.search_chat(USER_NAME)
    wh.select_chat(USER_NAME)
    wh.send_message("You are hacked!")


new_chat()

wh.close_browser()
