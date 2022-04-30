from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

URL='https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiTvqTSxurrAhXKIysKHXcJA3YYABAAGgJzZg&ae=2&ohost=www.google.com&cid=CAESQOD2azFiHSqAvnHtAlTpuCYUQjVHSSViQlmg7Bjj28meXqKiloBPSnoPA5dqmbQERZjSmpgDomtMvaItQx5dzZE&sig=AOD64_2eMatnOJNUrk1YjaAtPD2dqQHHbw&q&adurl&ved=2ahUKEwiq6JzSxurrAhXOQ30KHVCUBwAQ0Qx6BAgkEAE'

driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")
driver.get(URL)

# dropdown selector
# dropDown = driver.find_element_by_name("birthday_month")
# select = Select(dropDown)
# select.select_by_visible_text("Dec")
# time.sleep(2)
# select.select_by_visible_text("Jun")

# radio_button
radioSpace = driver.find_element_by_class_name("_5k_3")
button = radioSpace.find_element_by_tag_name("input")
print button.get_attribute("value")
button.click()


# button = radioSpace.find_element_by_id("u_0_7")
# button.click()
# button = radioSpace.find_element_by_id("u_0_8")
# button.click()
