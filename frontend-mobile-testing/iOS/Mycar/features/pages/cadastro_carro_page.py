from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CadastroCarrosPage(BasePage):

    BRAND_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Marca *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    MODEL_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Modelo *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    DESCRIPTION_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Versao *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    YEAT_INPUT = (By.XPATH, '//XCUIElementTypeCell[@name="Ano Modelo *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    REGISTER_BTN = (By.XPATH, '//XCUIElementTypeCell[@name="Cadastrar"]/XCUIElementTypeOther[2]/XCUIElementTypeOther')
    REGISTER_INPUT = '//XCUIElementTypeCell[@name="ATTRIBUTE *"]/XCUIElementTypeOther[2]/XCUIElementTypeOther'


    def replace_attribute(self,name):
        INPUT = self.CAR_REGISTER_INPUT.replace("ATTRIBUTE", name)
        locator = (By.XPATH, INPUT)
        return locator

    
    def register_screen_validate(self):
        super().wait_element_visibility(self.REGISTER_BTN)


    def set_brand(self,text):
        super().send_keys(self.CAR_REGISTER_INPUT("Marca *"),text)


    def set_model(self,text):
        super().send_keys(self.CAR_REGISTER_INPUT("Modelo *"),text)


    def set_description(self,text):
        super().send_keys(self.CAR_REGISTER_INPUT("Versao *"),text)


    def set_year(self,text):
        super().send_keys(self.CAR_REGISTER_INPUT("Ano Modelo *"),text)

    
    def click_on_register(self):
        super().click(self.CAR_REGISTER_INPUT("Cadastrar"))
    
    #ADD_BUTTON = driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='Meu Botão']")
    
 #   def click_on_add_btn(self):
 #       super().click(self.ADD_BUTTON)

 