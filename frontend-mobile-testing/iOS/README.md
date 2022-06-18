## Automacao iOS

#### Dependeicias necessarias para execucao local e remota (BrowserStack)
* Instalar Python 3
* Instalar appiun utilizando o comando
 - brew install appium

* Instalar Xcode (versao 13+  - 
* Instalar Command Line Tools for Xcode - 
* Instalar Appium inspector - (baixar o arquivo **Appium-Inspector-mac-2021.9.2.dmg**)
- Apos realizar o download do Inspector executar o comando
    'xattr -cr Appium-Inspector-mac-2021.9.2.dmg'

* Criar Simulador dentro do XCode(Caso o simulador esteja com o idioma **pt** modificar para **en**)
    * Criar simulador com a versao do iOS 9.3+

* Instalar .app do Simulador
* Instalar e inicializar postgreSQL utilizando os comandos
    'brew install postgress'
    'brew services start postgresql'

* Na raiz do diretorio do projeto executar o comando
    'pip3 install -r requirements.txt'


## POSSIVEIS PROBLEMAS

* Para resolver problema xcrun: error: unable to find utility "simctl", not a developer tool or in PATH ao inseir comando scrun simctl list
- Ir ao menu do Xcode>preferences>Locations
- Em Command Line Tools selecionar a verso do xCode. Exemplo xCode 13.3.1(13E500A)


## EXECUCAO DE TODOS OS TESTES COM REPORT
    1- Abra terminal
    2- Dentro da pasta 'frontend-mobile-testing/iOS', execute comando 'bash runTests.sh'
    3- Para ver o relatorio estara disponivel na pasta ExecutionReports apos a execucao da mesma.
    Obs: Cada vez que for executado o teste, o relatorio anterior é excluido para que seja gerado o relatorio atualizado da execucao atual