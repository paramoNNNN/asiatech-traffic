#!/usr/bin/env python3
import time
import os
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1366, 768))
display.start()

driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
driver.get('http://1544.ir')

driver.find_element_by_id('login').click()

# your username
elem = driver.find_element_by_id('txtUserName')
elem.send_keys("YOUR_USERNAME")

# your password
elem = driver.find_element_by_id('txtPassword')
elem.send_keys("YOUR_PASSWORD")

driver.find_element_by_id('btnLogin').click()
time.sleep(7)
try:
    driver.find_element_by_id('go_main').click()
except:
    os.system('notify-send "1544.ir" "Try Again!"')

elem = driver.find_element_by_id('ctl00_Content_curentGigService')
time.sleep(5)

os.system('notify-send "1544.ir" ' + elem.text)

driver.quit()
display.stop()
