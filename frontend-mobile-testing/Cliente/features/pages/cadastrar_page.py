from appium.webdriver.common.mobileby import MobileBy
from pages.base_page import BasePage


class CadastroPage(BasePage):
    
    REGISTER_CLIENT_INPUT = '//*[contains(@text, "ATTRIBUTE")]'


    def replace_attribute(self,name):
        INPUT = self.REGISTER_CLIENT_INPUT.replace("ATTRIBUTE", name)
        locator = (MobileBy.XPATH, INPUT)
        return locator


    def set_name_client(self,text):
        super().send_keys(self.replace_attribute("Nome"),text)


    def set_rg(self,text):
        super().send_keys(self.replace_attribute("RG"),text)


    def set_cpf(self,text):
        super().send_keys(self.replace_attribute("CPF"),text)

    
    def set_datanasc(self,text):
        super().send_keys(self.replace_attribute("Data de Nascimento"),text)


    def set_endereco(self,text):
        super().send_keys(self.replace_attribute("Endereço"),text)

    
    def set_numero(self,text):
        super().send_keys(self.replace_attribute("N°"),text)


    def set_bairro(self,text):
        super().send_keys(self.replace_attribute("Bairro"),text)

    
    def set_cep(self,text):
        super().send_keys(self.replace_attribute("CEP"),text)

    
    def set_cidade(self,text):
        super().send_keys(self.replace_attribute("Cidade"),text)


    def set_telefone(self,text):
        super().send_keys(self.replace_attribute("Telefone 1"),text)


    def set_email(self,text):
        super().send_keys(self.replace_attribute("E-mail"),text)


    def click_on_salvar_btn(self):
        super().click(self.replace_attribute("SALVAR"))


    def click_on_excluir_btn(self):
        super().click(self.replace_attribute("EXCLUIR"))

    
    def register_sucessfull(self):
        super().wait_element_visibility(self.replace_attribute("Cadastro efetuado com sucesso"))


    def click_on_ok_btn(self):
        super().click(self.replace_attribute("OK"))