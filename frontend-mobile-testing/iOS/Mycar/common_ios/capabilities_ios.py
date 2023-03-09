import os
import sys
from appium import webdriver
from hamcrest import assert_that, is_
#from common.apis.JIRA.jira import update_card_jira
PARENT_PATH = os.path.abspath('..')
if PARENT_PATH not in sys.path:
    sys.path.insert(0,PARENT_PATH)

path_app = PARENT_PATH
path_app = path_app + "/Mycar/common_ios/Mycar.app"

class Environment:
    def set_capabilities(context,scenario):
        BROWSER_STACK_CUSTOM_ID_IOS = "nomeAPP"
        desired_caps = {}

        #if context.config.userdata['type_execution'].upper() in 'BROWSERSTACK':
        #    print("ENTREI NO IF")
        #    directory = os.path.abspath("..")
        if context.config.userdata['type_execution'].upper() in 'BROWSERSTACK':
            directory = os.path.abs("..")
            os.system(directory+'/browserstack_local.sh')
            desired_caps['project'] = 'nomeProjeto'
            desired_caps['build'] = 'nomeBuild'
            desired_caps['name'] = scenario.name
            desired_caps['browserstack.debug'] = True
            desired_caps['app'] = BROWSER_STACK_CUSTOM_ID_IOS
            desired_caps['platformName'] = 'iOS'
            desired_caps['device'] = 'iPhone 11'
            desired_caps['os_version'] = '13'
            desired_caps['browserstack.local'] = context.user.config.userdata['execution_local_browserstack']
            desired_caps['autoGrantPermissions'] = True
            desired_caps['autoAcceptAlerts'] = True
            desired_caps['noReset'] = False
            desired_caps['automationName'] = 'XCUITest'
            desired_caps['realMobile'] = True
            context.driver = webdriver.Remote(
                context.config.userdata['appium_server_browserstack'], desired_caps)

        elif context.config.userdata['type_execution'].upper() in 'LOCAL':
            desired_caps['platformName'] = 'iOS'
            desired_caps['avd'] = 'iPhone 11'
            desired_caps['deviceName'] = 'iPhone 13'
            desired_caps['platformVersion'] = '15.5'
            desired_caps['udid'] = '0067B2F7-840F-4661-BAB0-B9EB5F1098CD'
            desired_caps['automationName'] = 'XCUITest'
            desired_caps['autoGrantPermissions'] = True
            desired_caps['autoAcceptAlerts'] = True
            desired_caps['locationServicesEnabled'] = True
            desired_caps['autoDismissAlerts'] = True
            desired_caps['noReset'] = False
            #desired_caps['bundleId'] = 'br.com.intermedium'
            desired_caps['newCommandTimeout'] = 6000
            #desired_caps['app'] = context.config.userdata['app_folder_location']
            desired_caps['app'] = path_app
            context.driver = webdriver.Remote(
                context.config.userdata['appium_server_local'], desired_caps
            )
                
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
                    