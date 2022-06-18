
# language: pt
Funcionalidade: Exportar Dados do Cliente


    @exportar_dados
    Cenário: Verifique que é exibidos opcoes de exportacao de dados do cliente
        Dado   Que estou na home do app
        E      Clico no menu
        Quando Clico em exportar dados
        Entao  Valido que é exibido todas as opcoes de exportar dados do cliente