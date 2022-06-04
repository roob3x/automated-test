from appium import webdriver
import os
import sys
PARENT_PATH = os.path.abspath('..')
if PARENT_PATH not in sys.path:
    sys.path.insert(0,PARENT_PATH)

path_apk = PARENT_PATH
path_apk = path_apk + "/Cliente/common/cadastro_clientes_teste.apk"

class Enviroment:
    def set_capabilities(context,scenario):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'br.com.dudstecnologia.cadastrodeclientes'
        desired_caps['appActivity'] = 'br.com.dudstecnologia.cadastrodeclientes.MainClientes'
        desired_caps['app'] = path_apk
        desired_caps['autoGrantPermissions'] = True
        desired_caps['autoAcceptAlerts'] = True
        desired_caps['automationName'] = 'UiAutomator2'
        context.driver = webdriver.Remote(context.config.userdata['appium_server_local'], desired_caps)