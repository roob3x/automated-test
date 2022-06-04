from behave import *
from pages.home_page import HomePage


@given('Que estou na home do app')
def step_impl(context):
    context.page_object = HomePage(context.driver)
    context.page_object.home_page_validate()


@given('Clico no menu')
def step_impl(context):
    context.page_object.click_on_register_client_btn()


@when('Clico em cadastrar novo')
def step_impl(context):
    context.page_object.click_on_new_register_btn()


@when('Clico em exportar dados')
def step_impl(context):
    context.page_object.click_on_exportar_dados()