from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class elementLink:
    '''
    This class provides stack representation to reach to the HTML element (or menu , button, textbox etc.)
    example:
            Home -> Master Repository
            Home -> System tree
    '''

    def __init__(self):
        self.elementStack = list()

    def get(self, Name):
        self.name = Name


driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")
driver.get("https://www.geeksforgeeks.org/")
driver.set_window_size(1552, 840)
driver.find_element(By.LINK_TEXT, "Sign In").click()
element = driver.find_element(By.LINK_TEXT, "Sign In")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# driver.find_element(By.CSS_SELECTOR, "#luser").click()
driver.find_element(By.ID, "luser").send_keys("uuu")
driver.find_element(By.ID, "password").send_keys("9999")
driver.find_element(By.CSS_SELECTOR, ".signin-button").click()
driver.find_element(By.CSS_SELECTOR, ".close").click()
driver.find_element(By.LINK_TEXT, "Sign In").click()
driver.find_element(By.CSS_SELECTOR, ".close").click()

# driver.get('https://www.geeksforgeeks.org/')
#
# button = driver.find_element_by_xpath("//a[contains(text(),'Sign In')]")
# button.click()
#
# try:
#     element = button.find_element_by_xpath("//input[@id='luser']")
#     element.send_keys('rrrr')
# except Exception:
#     element = driver.find_element_by_css_selector("#luser")
#     element.click()
#     element.send_keys('rrrr')


# time.sleep(5)
# element = driver.find_element_by_id('name')
# element.send_keys('suhrud')
# element = driver.find_element_by_id('password')
# element.send_keys('mcafee')
# element.send_keys(Keys.RETURN)
#
# time.sleep(5)
#
# element = driver.find_element_by_id('mfsLauncher')
# element.click()
#
# element=driver.find_element_by_id('PoliciesAndTasks_page')
# element.click()
#
# # element=driver.find_element(By.xpath ('otsID_Tabs.SYSTEMS')
# # element.click()
#
# inputElementGames = Select(driver.find_element_by_xpath("select[id='computerTable_filterList']")).options
# inputElementGames.select_by_visible_text('This Group and All Subgroups')
