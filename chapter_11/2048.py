#! python3
#
# 2048.py - automatically plays 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Firefox()
driver.get('https://gabrielecirulli.github.io/2048/')

keys_list = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

bodyElem = driver.find_element_by_tag_name('body')

for i in range(2000):
    bodyElem.send_keys(keys_list[random.randrange(0,4)])
