#!/usr/bin/env python3
import time
import os
import sys
from pyvirtualdisplay import Display
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')

display = Display(visible=0, size=(1366, 768))
display.start()

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
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

elem = driver.find_element_by_id('divGig0')
time.sleep(5)

os.system('notify-send "1544.ir" ' + elem.text)

driver.quit()
display.stop()
