import selenium
from selenium.webdriver.support.ui import Select
import configParser
import time

class systemTree():
    def __init__(self,driver):
        self.driver = driver
        self.parser = configParser.parser("config.json")
        self.config = self.parser.get_data()
    def go_to_system_tree(self):
        my_element='System Tree'
        self.driver.implicitly_wait(20)

        try:
            if self.driver.find_element_by_id("mfsLauncher").is_displayed():
                self.driver.find_element_by_id("mfsLauncher").click()
            eles = self.driver.find_elements_by_class_name("shortcutText")
            for ele in eles:
                if ele.text == my_element:
                    my_element = ele
            my_element.click()
            time.sleep(2)
            print("Pass - Clicking system tree section")
        except Exception:
            print("Failed to find system tree elements")

    def select_group(self,name):
        # self.driver.find_element_by_xpath("/html/body/form/div[9]/div[1]/div[3]/div[2]/div/div/div[1]/table/tbody/tr/td[1]/span/select").click()

        try:
            if self.driver.find_element_by_id("computerTable_filterList").is_displayed():
                dropDown = Select(self.driver.find_element_by_id("computerTable_filterList"))
                dropDown.select_by_visible_text(name)
                print('Pass - selected group in system tree')
        except Exception:
            print('Error- Failed to select group in system tree')

    def quick_find(self,system_name):
        self.driver.implicitly_wait(20)
        try:
            if self.driver.find_element_by_id("computerTable_quickFind").is_displayed():
                self.driver.find_element_by_id("computerTable_quickFind").send_keys(system_name)
            if self.driver.find_element_by_id("computerTable_quickFindButton").is_displayed():
                self.driver.find_element_by_id("computerTable_quickFindButton").click()
            print('Pass - filtered machine system name in system tree')
        except Exception:
            print('Error- Failed to find machine system name in system tree')

    def select_system(self):
        self.driver.find_element_by_xpath(self.config["selected_system_xpath"]).click()