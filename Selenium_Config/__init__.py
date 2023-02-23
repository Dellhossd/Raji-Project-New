from selenium import webdriver
import time

browser = webdriver.Firefox()
time.sleep(10)
browser.maximize_window()
time.sleep(10)
browser.get("https://google.com")
browser.close()

