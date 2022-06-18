from common_android.capabilities import Enviroment


def before_scenario(context,scenario):
    Enviroment.set_capabilities(context,scenario)


def after_scenario(context,scenario):
    context.driver.close_app()