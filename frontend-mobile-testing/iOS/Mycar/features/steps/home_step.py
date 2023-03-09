from behave import *
from pages.home_page import HomePage


@given('Que estou na home do app')
def step_impl(context):
    context.page_object = HomePage(context.driver)
    context.page_object.home_page_validate()


@when('Clico em Add')
def step_impl(context):
    context.page_object.click_on_add_btn()


@when('Preencho os dados do veiculo')
def step_impl(context):
    for row in context.table:
        context.page_object.set_brand(row['Marca'])
        context.valor = row['Marca']
        context.page_object.set_model(row['Modelo'])
        context.page_object.set_description(row['Versao'])
        context.page_object.set_year(row['Ano_Modelo'])


@when('Clico em cadastrar')
def step_impl(context):
    #context.page_object.register_screen_validate()
    #context.page_object.click_on_brand()
    context.page_object.click_on_register()

@then('Valido que o carro foi cadastrado com sucesso')
def step_impl(context):
    context.page_object.new_car_added_validate()
