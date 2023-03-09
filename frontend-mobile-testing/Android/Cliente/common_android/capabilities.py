from appium import webdriver
import os
import sys
from hamcrest import assert_that, is_
PARENT_PATH = os.path.abspath('..')
if PARENT_PATH not in sys.path:
    sys.path.insert(0,PARENT_PATH)

path_apk = PARENT_PATH
path_apk = path_apk + "/Cliente/common_android/cadastro_clientes_teste.apk"

class Enviroment:
    def set_capabilities(context,scenario):
        
        BROWSERSTACK_CUSTOM_ID_ANDROID = 'teste'

        if context.config.userdata['type_execution'].upper() in 'BROWSERSTACK':
            directory = os.path.abs("..")
            os.system(directory+'/browserstack_local.sh')
            desired_caps['browserstack.user'] = 'inserirlogin'
            desired_caps['browserstack.key'] = 'inserirsenha'
            desired_caps['project'] = 'nomeProjeto - Appium Android'
            desired_caps['build'] = 'nomeBuild - Android ' + \
                context.config.userdata['app_version']
            desired_caps['browserstack.debug'] = True
            desired_caps['app'] = BROWSERSTACK_CUSTOM_ID_ANDROID
            desired_caps['platformName'] = 'Android'
            desired_caps['device'] = 'Samsung Galaxy S10'
            desired_caps['os_version'] = '9.0'
            desired_caps['appPackage'] = 'nomeDoPacote'
            desired_caps['appActivity'] = 'nomeAcivity'
            desired_caps['browserstack.local'] = context.config.userdata['execution_local_browserstack']
            desired_caps['autoGrantPermissions'] = True
            desired_caps['AutoAcceptAlerts'] = True
            desired_caps['name'] = scenario.name
            context.driver = webdriver.Remote(
               context.config.userdata['appium_server_browserstack'], desired_caps)


        elif(context.config.userdata['type_execution'].upper() in 'LOCAL'):
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


    def execution_status(context, scenario):
        if context.config.userdata['type_execution'].upper() in 'BROWSERSTACK':
            try:
                assert_that(str(scenario.status), is_("Status.passed"))
                context.driver.execute_script(
                    'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                        {"status":"passed", "reason": "Passed"}}')
            except:
                context.driver.execute_script(
                    'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                        {"status":"failed", "reason": "Failed"}}')
