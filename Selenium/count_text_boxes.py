from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")

driver.get("https://mis.tgwdcw.in/Recruit.aspx")
driver.implicitly_wait(10)

# if driver.find_element_by_xpath("").is_displayed():
eles= driver.find_elements(By.CLASS_NAME,"input-text")
while len(eles):
    ele = eles.pop()
    if ele.tag_name != 'txtDOB':
        ele.send_keys("999")

    # driver.find_element_by_name("u_Fxa_338354").send_keys("Kothiya")
# print type(input_boxes)
# print len(input_boxes)
time.sleep(10)
driver.quit()
