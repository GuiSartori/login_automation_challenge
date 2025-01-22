"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""

# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from datetime import datetime
from funcoes import log_append, log_create

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    # print(f"Task ID is: {execution.task_id}")
    # print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.EDGE

    # Uncomment to set the WebDriver path
    bot.driver_path = r"C:\Users\guilh\Documents\BotCity\Drivers\msedgedriver.exe"

    # Abre o site da atividade
    bot.browse("https://practicetestautomation.com/practice-test-login/")

    # Implement here your logic...

    # Função para realizar a tentativa de login
    def tentativa_login(username, password, tentativas): # valores de usuário, senha e tentativas como parâmetros

        count_error = 0 # Contador do número de tentativas de login sem sucesso

        for i in range(tentativas): # loop com número de repetições definido pela variável 'tentativas'

            log_append(f"Iniciando {i+1} tentativa") # Registra o número da tentativa no log

            # Muda o username para o correto na última tentativa, para simular erros e acertos no login para a atividade
            if i+1 == tentativas:
                username = "student"
                log_append('Username alterado para "student"')
                log_append('Realizando tentativa de login com o username correto')

            # Insere o username
            log_append("Inserindo username")
            bot.wait(500)
            username_field = bot.find_element("//input[contains(@name, 'username')]", By.XPATH)
            username_field.send_keys(username)

            # Insere a senha
            log_append("Inserindo password")
            bot.wait(500)
            password_field = bot.find_element("//input[contains(@name, 'password')]", By.XPATH)
            password_field.send_keys(password)

            # Clica em submit
            log_append("Clickando no botão submit")
            bot.wait(500)
            submit_button = bot.find_element("//button[contains(@id, 'submit')]", By.XPATH)
            submit_button.click()

            bot.wait(1000)

            try: # Verifica se a mensagem de login sucedido é encontrada na página
                message = bot.find_element('//h1[text()="Logged In Successfully"]', By.XPATH)
                print(message.text) # Printa a mensagem de login sucedido
                log_append("Login sucedido")
                log_append("Finalizando a execução da automação...")
                break # Encerra o loop
            except: # Caso a mensagem de login sucedido não seja encontrada...
                log_append("Mensagem de login sucedido não encontrada.") # Registra mensagem indicando falha no login
                count_error += 1 # Itera o contador de tentativas com erro

        if count_error == tentativas: # Caso seja a última tentativa realizada...
            log_append(f"Foram realizadas {i+1} tentativas de login sem sucesso. Finalizando bot...") # Registra a quantidade de tentativas realizadas e sinaliza o fim da execução do bot

    log_create() # Cria o arquivo de log com a data e hora atuais como nome
    tentativa_login("student","Password123",3) # Tenta realizar o login com os parâmetros username, password e tentativas

    # Wait 3 seconds before closing
    bot.wait(2000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
