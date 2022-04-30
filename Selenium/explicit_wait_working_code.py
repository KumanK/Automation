from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)

# driver.get("https://leetcode.com/")
# driver.find_element_by_xpath("//*[@id=\"landing-page-app\"]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]/span").click()
# driver.find_element_by_id('id_login').send_keys("kkj28kumanj@gmail.com")
# driver.find_element_by_id('id_password').send_keys("virus@nov11@#$")
# driver.find_element_by_xpath("//*[@id=\"signin_btn\"]/div")
# driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/button/div").click()
# # ele = driver.find_element_by_xpath("//*[@id=\"question-app\"]/div/div[2]/div[2]/div[1]/div[2]/div[5]/button/div")
# wait = WebDriverWait(driver,20)
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/a").click()
# # ele = wait.until(Ec.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[5]/button/div")))
# ele = wait.until(Ec.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/a[10]/span[1]")))
# ele.click()



wait = WebDriverWait(driver,50)  # explicit wait
driver.get("https://www.hackerrank.com/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[3]/div/main/article/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div/a").click()
ele = wait.until(Ec.element_to_be_clickable((By.XPATH,"//*[@id=\"post-8330\"]/div/div/div[6]/div/div/div/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/div/a/img")))
ele.click()
time.sleep(10)
driver.quit()
