import selenium
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import configParser
import time

class actions():
    def __init__(self,driver):
        self.driver = driver

    def click_on_Actions(self):
        self.driver.implicitly_wait(10)
        ele=self.driver.find_element_by_css_selector(".actionPopupButton")
        # print(ele.text)
        # print(ele.id)
        # print(ele.is_selected)
        ele.click()

        # self.driver.find_element_by_class_name("actionMenuItem").click()
        # time.sleep(5)
        # try:
        #     self.driver.find_element_by_css_selector("#UIActionsButton").click()
        #     # if self.driver.find_element_by_id("UIActionsButton").is_displayed():
        #     #     pass
        # except Exception:
        #     print("Fail- not able to discover Actions button")

    def select_agent_and_click___Run_Client_Task_Now(self):
        self.driver.implicitly_wait(10)
        time.sleep(5)
        if self.driver.find_element_by_css_selector(".menubuttonbutton").is_enabled():
            self.driver.find_element_by_css_selector(".menubuttonbutton").click()
        time.sleep(2)
        act = ActionChains(self.driver)
        if self.driver.find_element_by_xpath("//*[@id='orion.core.body.tag']/div[5]/div[3]/div").is_displayed():
            Agent_loc = self.driver.find_element_by_xpath("//*[@id='orion.core.body.tag']/div[5]/div[3]/div")
            act.move_to_element(Agent_loc).perform()
        if self.driver.find_element_by_xpath("/html/body/div[6]/div[4]").is_displayed():
            Run_Client_Task_loc = self.driver.find_element_by_xpath("/html/body/div[6]/div[4]")
            act.move_to_element(Run_Client_Task_loc).click().perform()

    def run_solidcore_client_task(self,name,UID='3333'):
        automation_task_type = 'demo-automation-task'
        time.sleep(5)
        if self.driver.find_element_by_xpath("/html/body/form/div[7]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]").is_displayed():
            self.driver.find_element_by_xpath("/html/body/form/div[7]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]").click()
        time.sleep(2)
        if self.driver.find_element_by_id("id_TaskTypes").is_displayed():
            eles = self.driver.find_elements_by_class_name("orionListItem")
            for ele in eles:
                if ele.text == name:
                    ele.click()
                    break

        if self.driver.find_element_by_id("id_TaskNames").is_displayed():
            ele= self.driver.find_element_by_class_name("orionListItemSelected")
            if ele.text == automation_task_type:
                ele.click()
        time.sleep(1)
        if self.driver.find_element_by_id("run.button").is_enabled():
            self.driver.find_element_by_id("run.button").click()
            print("Pass- clicking Run Client Task Now button")