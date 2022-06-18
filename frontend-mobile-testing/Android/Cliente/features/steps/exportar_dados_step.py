from hamcrest import assert_that, is_
from pages.exportar_dados_page import ExportardadosPage


@then('Valido que é exibido todas as opcoes de exportar dados do cliente')
def step_impl(context):
    context.page_object = ExportardadosPage(context.driver)
    context.page_object.exportar_dados_validate()
    context.page_object.backup_btn_validate()
    context.page_object.restaurar_btn_validate()