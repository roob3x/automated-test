# language: pt
Funcionalidade: Cadastro Cliente


    @cadastro @sucesso @sanity
    Cenário: Verifique que é possível cadastrar um novo cliente
        Dado   Que estou na home do app
        E      Clico no menu
        Quando Clico em cadastrar novo
        E      Preencho os dados do cliente
               | Nome | Rg         | Cpf         | Datanasc | Endereco | Num | Bairro   | Cep      | Cidade   | Telefone   | Email             |
               | Rob  | 7483683    | 32107501300 | 26       | cabus    | 16  | candeias | 54440350 | jaboatao | 8199999999 | e.nain@hotmai.com |
        E      Clico em salvar
        Então  Valido que o cliente foi cadastrado com sucesso