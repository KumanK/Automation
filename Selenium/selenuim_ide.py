# Generated by Selenium IDE

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest2():
    def setup_method(self):
        self.driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_test2(self):
        self.driver.get("https://www.geeksforgeeks.org/")
        self.driver.set_window_size(1552, 840)
        tmp = self.driver.find_element_by_class_name('leftBarList')
        tmp.find_element(By.LINK_TEXT, "Tutorial Library").click()
        tmp.find_element(By.LINK_TEXT, "Pandas Tutorial").click()
        # self.driver.execute_script("window.scrollTo(0,203)")
        # self.driver.execute_script("window.scrollTo(0,305)")
        # self.driver.find_element(By.LINK_TEXT, "Operations").click()
        # self.vars["window_handles"] = self.driver.window_handles
        # self.driver.find_element(By.LINK_TEXT, "Pandas GroupBy").click()
        # self.vars["win1440"] = self.wait_for_window(2000)
        # self.driver.switch_to.window(self.vars["win1440"])


O = TestTest2()
O.setup_method()
O.test_test2()