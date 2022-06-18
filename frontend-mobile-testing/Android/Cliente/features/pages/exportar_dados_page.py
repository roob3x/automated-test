from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage


class ExportardadosPage(BasePage):

    EXPORTAR_DADOS_BTN = (MobileBy.ID, 'br.com.dudstecnologia.cadastrodeclientes:id/btnExportar')
    BACKUP_BTN = (MobileBy.ID, 'br.com.dudstecnologia.cadastrodeclientes:id/btnBackup')
    RESTAURAR_BTN = (MobileBy.ID, 'br.com.dudstecnologia.cadastrodeclientes:id/btnRestaurar')


    def exportar_dados_validate(self):
        super().wait_element_visibility(self.EXPORTAR_DADOS_BTN)

    
    def backup_btn_validate(self):
        super().wait_element_visibility(self.BACKUP_BTN)


    def restaurar_btn_validate(self):
        super().wait_element_visibility(self.RESTAURAR_BTN)