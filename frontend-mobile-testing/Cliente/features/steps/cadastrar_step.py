from behave import *
from pages.cadastrar_page import CadastroPage
from common.utils import *


@when('Preencho os dados do cliente')
def step_impl(context):
    context.page_object = CadastroPage(context.driver)
    for row in context.table:
        context.page_object.set_name_client(row['Nome'])
        context.page_object.set_rg(row['Rg'])
        context.page_object.set_cpf(row['Cpf'])
        context.page_object.set_datanasc(get_custom_birhtday(row['Datanasc']))
        context.page_object.set_endereco(row['Endereco'])
        context.page_object.set_numero(row['Num'])
        context.page_object.set_bairro(row['Bairro'])
        context.page_object.set_cep(row['Cep'])
        context.page_object.set_cidade(row['Cidade'])
        context.page_object.set_telefone(row['Telefone'])
        context.page_object.set_email(row['Email'])


@when('Clico em salvar')
def step_impl(context):
    context.page_object.click_on_salvar_btn()


@then('Valido que o cliente foi cadastrado com sucesso')
def step_impl(context):
    context.page_object.register_sucessfull()
    context.page_object.click_on_ok_btn()