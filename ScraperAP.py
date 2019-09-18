from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from datetime import datetime, timedelta
import os
from time import sleep

list=[]
url = "https://www.ap7am.com/telugu-news"

driver = webdriver.Chrome('/Users/akhilavemuganti/Downloads/chromedriver.exe')
driver.maximize_window()
driver.get(url)
time.sleep(5)

elements=driver.find_elements_by_class_name('titlelist')
for item in elements:
    list.append(item.text)

print(list)
print(len(list))
driver.close()


