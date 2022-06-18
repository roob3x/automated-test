from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, is_


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

    def find_element(self,element):
        return self.driver.find_element(*element)


    def find_elements(self,element):
        return self.driver.find_elements(*element)


    def get_text_element(self,locator):
        return self.find(locator).text


    def scroll_down_android(self,value):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollToEnd('+value+')')

    
    def scroll_down_until_element_is_not_present(self,element):
        x = 0
        while x<=20:
            if len(self.find_elements(element)) == 1:
                break
            self.scroll_down_android('1')
            time.sleep(1)
            x = x + 1

    
    def scroll_down_until_element_is_not_present_ios(self,element):
        x = 0
        while x<=20:
            if len(self.find_elements(element)) == 1:
                break
            self.scroll_down_ios()
            time.sleep(1)
            x = x + 1

    
    def scroll_down(self):
        self.driver.execute_script('mobile: scroll', {'direction': 'down'});


    def move_carousel(self, eli1, eli2):
        element1 = self.find_element(eli1)
        element2 = self.find_element(eli2)
        self.long_press(element1,element2)

    
    def long_press(self,eli1):
        action = TouchAction(self.driver)
        action.tap(eli1).peform().release


    def custom_implicity_wait(self,element):
        i = 0
        state = False
        elementoExiste = len(self.driver.find_elements(*element))
        while i<=40:
            elementoExiste = len(self.driver.find_elements(*element))
            time.sleep(0.5)
            if(elementoExiste > 0):
                state = True
                break
            i+=1


    def is_displayed(self,element):
        elementVisible = self.find_element(element)
        return elementVisible.is_displayed()


    def validate_expected_text(self, element, textExpected):
        assert_that(self.get_text_element(element),
            is_(textExpected))


    def move_to_element(self,locator):
        elemento = self.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', elemento)
        
