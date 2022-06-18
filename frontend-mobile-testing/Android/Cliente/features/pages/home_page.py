from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage


class HomePage(BasePage):
    NOONE_CLIENT_TITLE =  (MobileBy.XPATH, '//*[contains(@text, "Nenhum cliente cadastrado")]')
    REGISTER_CLIENT_BTN = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'+
    'android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton')
    NEW_REGISTER_BTN = (MobileBy.XPATH, '//*[contains(@text, "Cadastrar Novo")]')
    EXPORTAR_DADOS_BTN = (MobileBy.XPATH, '//*[contains(@text, "Exportar Dados")]')


    def home_page_validate(self):
        super().wait_element_visibility(self.NOONE_CLIENT_TITLE)

    
    def click_on_register_client_btn(self):
        super().click(self.REGISTER_CLIENT_BTN)

    
    def click_on_new_register_btn(self):
        super().click(self.NEW_REGISTER_BTN)


    def click_on_exportar_dados(self):
        super().click(self.EXPORTAR_DADOS_BTN)