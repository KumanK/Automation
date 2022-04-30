import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

import json

class getDriver:
    '''
    Initiate an instance of webDriver and provide to user
    '''
    def __init__(self,URL):
        print 'URL= getDriver : ' + URL
        try:
            self.driver = webdriver.Chrome("C:\Users\kkuman.CORPZONE\Downloads\chromedriver_win32/chromedriver.exe")
            self.driver.get(URL)
        except Exception:
            print 'getDriver- constructor : --> Got the selenium driver exception'
            print traceback.format_exc()
            exit(-1)

class loginAttemp(getDriver):
    '''
    this class provides functionality to search 'sign in' button/link.
    Class method should be able to find an element based on different selenium searching methods

    Once button is found try to login with username and password
    '''

    def __init__(self, URL, username, password):
        print 'URL: '+URL
        getDriver.__init__(self, URL)
        self.user=username
        self.pas=password

    def findTheButton(self,property):
        '''

        :param driver: for which instance of browser we needs to find button
        :param property: any property id, name, css, xpath
        :return: return driver instance if operation is successful
        '''
        try:
            self.button = self.driver.find_element(By.CSS_SELECTOR, property)
            self.button.click()
            return True
        except Exception:
            print 'loginAttemp->findTheButton() : did not found matching element-By.CSS_SELECTOR'
        try:
            self.button = self.driver.find_element(By.CLASS_NAME, property)
            self.button.click()
            return True
        except Exception:
            print 'loginAttemp->findTheButton() : did not found matching element-By.CLASS_NAME'
        try:
            self.button = self.driver.find_element(By.XPATH, property)
            self.button.click()
            return True
        except Exception:
            print 'loginAttemp->findTheButton() : did not found matching element-By.XPATH'
        try:
            self.button = self.driver.find_element(By.LINK_TEXT, property)
            self.button.click()
            return True
        except Exception:
            print 'loginAttemp->findTheButton() : did not found matching element-By.LINK_TEXT'
        return False

    def login(self,userNameLoc,passwdLoc):
        try:
            self.usernameLoc = self.driver.find_element(By.CSS_SELECTOR, userNameLoc)
            self.passwordLoc = self.driver.find_element(By.CSS_SELECTOR, passwdLoc)
        except Exception:
            print 'loginAttemp->login() : did not found matching element-By.CSS_SELECTOR'

        try:
            self.usernameLoc = self.driver.find_element(By.CLASS_NAME, userNameLoc)
            self.passwordLoc = self.driver.find_element(By.CLASS_NAME, passwdLoc)
        except Exception:
            print 'loginAttemp->login() : did not found matching element-By.CLASS_NAME'

        try:
            self.usernameLoc = self.driver.find_element(By.XPATH, userNameLoc)
            self.passwordLoc = self.driver.find_element(By.XPATH, passwdLoc)
        except Exception:
            print 'loginAttemp->login() : did not found matching element-By.XPATH'

        try:
            self.usernameLoc = self.driver.find_element(By.LINK_TEXT, userNameLoc)
            self.usernameLoc.send_keys(self.user)
            self.passwordLoc = self.driver.find_element(By.LINK_TEXT, passwdLoc)
            self.passwordLoc.send_keys(self.pas)
        except Exception:
            print 'loginAttemp->login() : did not found matching element-By.LINK_TEXT'

        try:
            self.usernameLoc = self.driver.find_element(By.ID, userNameLoc)
            self.usernameLoc.send_keys(self.user)
            self.passwordLoc = self.driver.find_element(By.ID, passwdLoc)
            self.passwordLoc.send_keys(self.pas)
        except Exception:
            print 'loginAttemp->login() : did not found matching element-By.ID'

class findPath:
    '''
    class intend to create a dynamic link to reach to an HTML page object
    Map of the web location is assumed to be created in JSON fashion
    '''

    def __init__(self,config):
        with open(config,'r') as f:
            self.chart=json.load(f)
            print "Loaded config file : "+ config
            print "chart prepared : " + str(self.chart)

    def getMeLink(self,name):
        try:
            t=self.chart[name]
            print "name is found: " + name
            stri=self.chart["Flows"][name]
            L=stri.split("->")
            # print L

            def func(arg):
                return self.chart[arg]
            Link = list(map(func,L))
            # print Link, L
            return Link

        except KeyError:
            print "name is not found: Cannot create a link to reach the element"


class redirectTo(getDriver):

    def __init__(self,URL):
        getDriver.__init__(self,URL)

    def redirect(self,property):
        try:
            self.element = self.driver.find_element(By.CSS_SELECTOR, property)
            self.element.click()
        except Exception:
            print 'redirectTo->redirect() : did not found matching element-By.CSS_SELECTOR'
        try:
            self.element = self.driver.find_element(By.LINK_TEXT, property)
            self.element.click()
        except Exception:
            print 'redirectTo->redirect() : did not found matching element-By.LINK_TEXT'
        try:
            self.element = self.driver.find_element(By.ID, property)
            self.element.click()
        except Exception:
            print 'redirectTo->redirect() : did not found matching element-By.ID'

        try:
            self.element = self.driver.find_element(By.XPATH, property)
            self.element.click()
        except Exception:
            print 'redirectTo->redirect() : did not found matching element-By.XPATH'


