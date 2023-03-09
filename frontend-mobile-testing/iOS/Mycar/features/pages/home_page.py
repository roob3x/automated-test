#from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage
#from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    HOME_PAGE_TITLE =  (By.XPATH, '//XCUIElementTypeStaticText[@name="Meus Carros"]')
    ADD_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Add"]')
    BRAND_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Marca *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    MODEL_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Modelo *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    DESCRIPTION_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Versao *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    YEAT_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Ano Modelo *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    REGISTER_BTN = (By.XPATH, '//XCUIElementTypeCell[@name="Cadastrar"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    REGISTER_INPUT = '//XCUIElementTypeCell[@name="ATTRIBUTE *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther'
    NEW_CAR_LIST = (By.XPATH, '//XCUIElementTypeStaticText[@name="Compass"]')


    def replace_attribute(self,name):
        INPUT = self.REGISTER_INPUT.replace("ATTRIBUTE", name)
        locator = (By.XPATH, INPUT)
        return locator


    def home_page_validate(self):
        super().wait_element_visibility(self.HOME_PAGE_TITLE)


    def new_car_added_validate(self):
        super().wait_element_visibility(self.NEW_CAR_LIST)

    
    def click_on_add_btn(self):
        super().click(self.ADD_BUTTON)

    def register_screen_validate(self):
        super().wait_element_visibility(self.REGISTER_BTN)


    def click_on_brand(self):
        super().click(self.BRAND_INPUT)


    def set_brand(self,text):
        super().send_keys(self.BRAND_INPUT,text)


    def set_model(self,text):
        super().send_keys(self.MODEL_INPUT,text)


    def set_description(self,text):
        super().send_keys(self.DESCRIPTION_INPUT,text)


    def set_year(self,text):
        super().send_keys(self.YEAT_INPUT,text)

    
    def click_on_register(self):
        super().click(self.REGISTER_BTN)