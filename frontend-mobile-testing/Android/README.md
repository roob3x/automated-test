## automated-tests

## DOWNLOADS
    Instalar python3: https://www.python.org/downloads/ 
    Appium Desktop: é a interface da ferramenta Appium que será o foco do nosso workshop. O download está disponível aqui:
    JDK (JAVA Development Kit): https://www.java.com/pt_BR/download/

    Android Studio: é um pacote do Android Studio que possibilita que possamos instanciar dispositivos móveis de várias configurações e modelos de forma emulada e em vários níveis de API. Para isso, é preciso baixar o Android Studio e, durante o setup, marcar a opção de instalar também o AVD: https://developer.android.com/studio/index.html?hl=pt-br

## Criar emulador a partir do Android Studio
    Dentro do android studio na sessao de Device Manager escolha opcao de create device
    Versao de OS: Optar por OS mais recente. a nao ser que exista alguma incopatibilidade para algo em especifico para a necessidade de usar uma versao mais anteriror.
    Apos instalacao do emulador, voce estara apto para inicia-lo.
    Instalar .apk debug no emulador. temos duas opcoes:
    Arrastar a apk ate o emulador
    Abra o teriminal e entre na pasta onde esta apk por exemplo: cd Usr/Downloads em seguida instale atraves do adb com o seguinte comando: adb install cadastro_clientes_teste.apk
    
## IDE
    para Python, sugiro PyCharm ou VSCode. Links abaixo para download:

    PyCharm: https://www.jetbrains.com/pycharm/

    VSCode: https://code.visualstudio.com/

    Depois de fazer o download de todo o conteúdo, agora podemos avançar com o setup do ambiente. Podemos configurar as variáveis de ambiente à nível de sistema (abaixo eu deixo detalhado como fazer para cada SO) e também podemos fazer de maneira bem mais simplificada, onde explico melhor após o detalhe de setup para cada SO.

## Forma simplificada configurar variaveis de ambiente no Mac

    Se você quiser simplificar a sua configuração de ambiente, é só utilizar o atalho de configuração do Appium e inserir manualmente os caminhos para as suas variáveis ANDROID_HOME e JAVA_HOME. Esta etapa é bem mais simples e da mesma forma efetiva para uso da ferramenta. Basta seguir os passos adiante:

    Abra sua ferramenta Appium Desktop e clique no botão "Edit Configurations".

    Quando você clicar em "Edit Configurations", um popup vai abrir com 2 campos: ANDROID_HOME e JAVA_HOME. É só você identificar estes caminhos na sua máquina (no setup de configuração para cada SO eu deixei comandos e dicas para obter estes valores), copiar e colar nestes campos e em seguida clicar em "Save and Restart". Pronto, configuração do Appium realizada com sucesso :)

    no campo de ANDROID_HOME inserir -> seuUsuario/Library/Android/sdk em JAVA_HOME -> Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk/Contents/Home

    Instalando o Appium A instalação do Appium é bastante simples e não requer configuração adicional - além da do Android e do JDK. Basta baixar o Appium Desktop na página oficial do Appium(como no link do começo do documento) ou via linha de comando através do terminal:

    npm install -g appium ATENÇÃO: Não instale o Appium com sudo.

✨ Dica - O que é npm?

Npm é o gerenciador de downloads para pacotes node.js.

Como validar se tudo tá configurado ou se falta algo? Uma funcionalidade bem legal que o Appium oferece é o pacote Appium-doctor, cuja finalidade é conferir o checklist necessário para que seu ambiente funcione. Caso algo esteja faltando, o Appium-doctor te lista exatamente o que falta. Ele também confirma o que tá configurado como esperado. Para instalá-lo, é só instalar o pacote npm no seu terminal:

npm install -g appium-doctor --android

Depois de instalado o Appium-doctor, é só fazer a chamada via terminal:

appium-doctor Abaixo segue um exemplo de como é o retorno do Appium-doctor via terminal:

➜ bin appium-doctor info AppiumDoctor Appium Doctor v.1.10.0 info AppiumDoctor ### Diagnostic for necessary dependencies starting ### info AppiumDoctor ✔ The Node.js binary was found at: /usr/local/bin/node info AppiumDoctor ✔ Node version is 8.11.4 WARN AppiumDoctor ✖ Xcode is NOT installed! info AppiumDoctor ✔ Xcode Command Line Tools are installed in: /Library/Developer/CommandLineTools info AppiumDoctor ✔ DevToolsSecurity is enabled. info AppiumDoctor ✔ The Authorization DB is set up properly. info AppiumDoctor ✔ Carthage was found at: /usr/local/bin/carthage info AppiumDoctor ✔ HOME is set to: /Users/BEZERRA WARN AppiumDoctor ✖ ANDROID_HOME is NOT set! WARN AppiumDoctor ✖ JAVA_HOME is NOT set! WARN AppiumDoctor ✖ adb could not be found because ANDROID_HOME is NOT set! WARN AppiumDoctor ✖ android could not be found because ANDROID_HOME is NOT set! WARN AppiumDoctor ✖ emulator could not be found because ANDROID_HOME is NOT set! WARN AppiumDoctor ✖ Bin directory for $JAVA_HOME is not set info AppiumDoctor ### Diagnostic for necessary dependencies completed, 7 fixes needed. ###

Tudo que estiver acompanhado do símbolo ✔ significa que está instalado corretamente. Tudo que estiver acompanhado do símbolo ✖ significa que NÃO está instalado ou identificado. Esses casos você deve ajustar.

O pacote do Xcode é específico para iOS, então, para Android, não devemos nos preocupar.

Checklist de tudo o que fizemos até agora Se você chegou até aqui, significa que provavelmente o seu setup está pronto e agora você já pode usar todos os recursos do Appium! Só para checar, instalamos e configuramos:

Appium Desktop ✔ 
Android Studio (pacote AVD) ✔ 
JAVA ✔ 
IDE ✔ 
Configuração de variáveis de ambiente ✔
Python ✔

## CONFIGURANDO CAPABILITIES APPIUM
    Acessar o appiu e clicar em start Server

    Clicar na lupa.(ao passar o mouse sera exibido "Start Inspector Session")

    Em Desired capabitilies passar os seguinte parametros e valores e salvar

    platformName(text): Android

    deviceName(text): emulator-5554

    AutomationName(text): uiautomator2

    appPackage(text): br.com.dudstecnologia.cadastroclientes

    appActivity(text): br.com.dudstecnologia.cadastrodeclientes.MainClientes

    Feito isso sua maquina esta preparada para iniciar a sessao no appium e com isso podera inspecionar os elementos

## Instalacao do aplicativo no emulador
    Comandos ADB ADB é uma abreviação para Android Debug Brigde. Grosseiramente traduzindo, é uma ferramenta que faz uma "ponte" de comunicação entre o seu computador e o seu dispositivo móvel Android através de linhas de comando. Através do ADB, é possível que possamos manipular o dispositivo através de comandos, de forma muito prática, como:

    Instalar/desinstalar aplicativos; Mudar configurações internas, como: tempo de desligar tela, bloqueio/desbloqueio de tela, etc. Habilitar/desabilitar funções de conexões, como: wifi, dados, modo avião. Transferência/manipulação de arquivos; Reiniciar e desligar o dispositivo - não funciona para ligá-lo (mas isso pode ser resolvido através de frameworks). É também possível automatizar algumas atividades de rotina combinando comandos ADB e Python Script.

    Links importantes desta seção: Um pouco mais sobre comandos ADB: https://developer.android.com/studio/command-line/adb?hl=pt-br Um pouco Python Script: https://realpython.com/run-python-scripts/

## INSTALANDO DEPENDENCIAS DO PROJETO

- Na Raiz do projeto instalar as dependencias com "pip install -r requirements.txt"

## EXECUCAO DE TODOS OS TESTES COM REPORT
    1- Abra terminal
    2- Dentro da pasta 'frontend-mobile-testing/Android', execute comando 'bash runTests.sh'
    3- Para ver o relatorio estara disponivel na pasta ExecutionReports apos a execucao da mesma.
    Obs: Cada vez que for executado o teste, o relatorio anterior é excluido para que seja gerado o relatorio atualizado da execucao atual