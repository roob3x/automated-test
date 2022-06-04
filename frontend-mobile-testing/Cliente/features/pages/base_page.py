from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver = driver


    def wait_for(self,condition,sec = 20):
        return WebDriverWait(self.driver, sec).until(condition)
    

    def click(self, locator):
        self.wait_for(EC.element_to_be_clickable(locator)).click()


    def send_keys(self,locator,text):
        self.wait_for(EC.visibility_of_element_located(locator)).send_keys(text)


    def wait_until(self,condition,seconds):
        return WebDriverWait(self.driver,seconds).until(condition)


    def wait_element_visibility(self,locator):
        element = self.wait_until(EC.visibility_of_element_located(locator),60)
        return element

    
    def find(self,locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        return element


    def get_text_element(self,locator):
        return self.find(locator).text