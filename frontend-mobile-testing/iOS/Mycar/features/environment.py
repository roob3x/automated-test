from common_ios.capabilities_ios import Environment
import time


def before_scenario(context,scenario):
    Environment.set_capabilities(context,scenario)


def after_scenario(context,scenario):
    time.sleep(5)
    context.driver.quit()
