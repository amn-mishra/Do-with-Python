from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as gui
import time

#Enter your message.
message = "hello"

#Enter numbers with country code without + sign and without space.
numbers = []

browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")
time.sleep(10)

for i in numbers:
	url = browser.get("https://api.whatsapp.com/send?phone={}&text={}".format(i,message))
	time.sleep(5)
	chat_btn = browser.find_element_by_id('action-button')
	chat_btn.click()
	time.sleep(5)
	whatsap_web = browser.find_element_by_link_text("use WhatsApp Web")
	whatsap_web.click()
	time.sleep(8)
	gui.press("enter")
	time.sleep(8)