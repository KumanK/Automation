from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")
driver.get('https://www.geeksforgeeks.org/')

# Sign_In_button = driver.find_element(By.CSS_SELECTOR, '.login-modal-btn')
# Sign_In_button = driver.find_element_by_class_name('header-main__left-list-item')
# print Sign_In_button.text
# Sign_In_button = driver.find_element_by_class_name('login-modal-btn')
# print Sign_In_button.text
# time.sleep(5)

Sign_In_button = driver.find_element_by_link_text('Sign In')
# print Sign_In_button
Sign_In_button.click()
time.sleep(10)
# print elementSel
# elementSel.click()
# entries = Menu.find_element_by_tag_name("li")
# algo = entries.find_element("Algorithms")
# t = entries.fin('data-expandable','true')

# k = t.find_element_by_tag_name('li')
# print k.get_attribute('span')
# print algo

# print dir(entries)
# entries.click()
# print dir(algo)
# for entry in entries:
#     print entry


# list = Select(driver.find_element_by_xpath("//select[id='header-main__list-item selected']")).options
# list.select_by_visible_text('Placement Course')


# element = driver.find_element_by_class_name('material-icons header-main__list-item-caret')
# element.click()
driver.close()