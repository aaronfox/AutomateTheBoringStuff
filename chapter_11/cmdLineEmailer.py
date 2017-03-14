#! python3
#
# cmdLineEmailer.py - takes an email address and a string of text and emails it
# using yahoo's mailing client

import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##from selenium.webdriver.common.by import By
##from selenium.common.exceptions import TimeoutException

emailRecipient = ""
message = ""

print(len(sys.argv))
if len(sys.argv) > 1:
    emailRecipient = sys.argv[1]
    message = ' '.join(sys.argv[2:])
else:
    print("Usage: cmdLineEmailer.py email [message-to-send]")

driver = webdriver.Firefox()
driver.get('http://yahoo.com')
delay = 2 # seconds
#time.sleep(delay)
##try:
##    mailElement = WebDriverWait(driver, delay).until(
##        EC.presence_of_element_located((By.ID,
##            driver.find_element_by_id(
##            'uh-mail-link'))))
##except TimeoutException:
##    print('timed out waiting for page to load')

mailButton = driver.find_element_by_id('uh-mail-link')
mailButton.click()

driver.implicitly_wait(delay)
time.sleep(delay)

#usernameInput = driver.find_element_by_id('login-username')
usernameInput = driver.find_element_by_css_selector('#login-username')
usernameInput.click()
usernameInput.send_keys('*****@yahoo.com')
usernameInput.send_keys(Keys.ENTER)

time.sleep(delay)
passwordInput = driver.find_element_by_css_selector('#login-passwd')
passwordInput.send_keys('*****')
passwordInput.send_keys(Keys.ENTER)

time.sleep(delay)
time.sleep(7)
composeButton = driver.find_element_by_css_selector('#Compose')
composeButton.click()

time.sleep(delay)
# toBoxDict = driver.switch_to_active_element()
# toBox = toBoxDict["value"]
# toBox.send_keys('Bob.smith@yahoo.com')
# toBox.send_keys(Keys.TAB)
toBox = driver.find_element_by_css_selector('#to-field')
toBox.send_keys(emailRecipient)#'Bob.Smith@yahoo.com')

subjectBox = driver.find_element_by_css_selector('#subject-field')
subjectBox.send_keys('SUBJECT')

contentBox = driver.find_element_by_css_selector('#rtetext')
contentBox.click()
contentBox.send_keys(message)#'WOO WE MADE IT BRO!')
contentBox.send_keys(Keys.CONTROL + Keys.ENTER)

##sendButton = driver.find_element_by_partial_link_text('Send')
##sendButton.click()

