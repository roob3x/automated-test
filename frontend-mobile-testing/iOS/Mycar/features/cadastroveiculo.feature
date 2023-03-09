# language: pt
Funcionalidade: Cadastro Veiculo


    @cadastro @sucesso @sanity
    Cenário: Verifique que é possível cadastrar um novo veiculo
        Dado   Que estou na home do app
        Quando Clico em Add
        Quando Preencho os dados do veiculo
               | Marca | Modelo     | Versao         | Ano_Modelo |
               | Jeep  | Compass    | Longitude 2.0  | 2023       |
        Quando Clico em cadastrar
        Então  Valido que o carro foi cadastrado com sucesso