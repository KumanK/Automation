from selenium import webdriver
import configParser
import selenium

class login():
    def __init__(self):
        self.parser = configParser.parser("config.json")
        self.config = self.parser.get_data()
        self.driver = webdriver.Chrome(self.config['chrome_webdriver_location'])
        print("Info - web driver located successfully")
        # self.driver.
    def load_home_page(self,URL):
        self.URL=URL
        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)
        try:
            if self.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").is_displayed():
                print("Clicking Advanced button")
                self.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()
            if self.driver.find_element_by_id("proceed-link").is_displayed():
                print("Proceeding to epo page")
                self.driver.find_element_by_id("proceed-link").click()
        except Exception:
            print("Not able to locate Advanced button and proceed link")
            print ("Trying login attempt")

        try:
            if self.driver.find_element_by_id("name").is_displayed():
                self.driver.find_element_by_id("name").send_keys(self.config['epo_username'])
            if self.driver.find_element_by_id("password").is_displayed():
                self.driver.find_element_by_id("password").send_keys(self.config['epo_password'])
            if self.driver.find_element_by_id("login.button").is_enabled():
                self.driver.find_element_by_id("login.button").click()
            print("Successfully logged in ")
            self.driver.maximize_window()
            return self.driver
        except Exception:
            print("Not able to locate ePO login locators")
            print ("Failed to login")
            return False

