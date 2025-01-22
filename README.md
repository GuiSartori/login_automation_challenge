Aqui está um exemplo de README para o seu projeto de automação de login utilizando BotCity:

---

# Automação de Login com BotCity

Este projeto é uma automação de login utilizando a biblioteca BotCity para interagir com a web. O script realiza tentativas de login em um site de teste e registra as ações em um arquivo de log.

## Pré-requisitos

- Python 3.x
- Bibliotecas necessárias: `botcity`, `datetime`
- WebDriver para o navegador utilizado (Edge, neste caso)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/SeuUsuario/login_automation_challenge.git
    cd login_automation_challenge
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Baixe e configure o WebDriver para o navegador que você deseja utilizar (Edge, neste caso).

## Uso

1. Configure o caminho do WebDriver no script `bot.py`:
    ```python
    bot.driver_path = r"C:\Caminho\Para\Seu\WebDriver\msedgedriver.exe"
    ```

2. Execute o script:
    ```bash
    python bot.py
    ```

## Estrutura do Código

- **Importações**: Importa as bibliotecas necessárias para a automação web e integração com o BotCity Maestro SDK.
- **Função `main`**: Configura o bot, abre o site de login e chama a função de tentativa de login.
- **Função `tentativa_login`**: Realiza tentativas de login com os parâmetros fornecidos (username, password, tentativas) e registra as ações em um arquivo de log.
- **Função `log_create`**: Cria um arquivo de log com a data e hora atuais como nome.
- **Função `log_append`**: Adiciona mensagens ao arquivo de log com um timestamp.

## Exemplo de Código

```python
from botcity.web import WebBot, Browser, By
from datetime import datetime
from funcoes import log_append, log_create
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.EDGE
    bot.driver_path = r"C:\Caminho\Para\Seu\WebDriver\msedgedriver.exe"
    bot.browse("https://practicetestautomation.com/practice-test-login/")

    def tentativa_login(username, password, tentativas):
        count_error = 0
        for i in range(tentativas):
            log_append(f"Iniciando {i+1} tentativa")
            if i+1 == tentativas:
                username = "student"
                log_append('Username alterado para "student"')
                log_append('Realizando tentativa de login com o username correto')

            log_append("Inserindo username")
            bot.wait(500)
            username_field = bot.find_element("//input[contains(@name, 'username')]", By.XPATH)
            username_field.send_keys(username)

            log_append("Inserindo password")
            bot.wait(500)
            password_field = bot.find_element("//input[contains(@name, 'password')]", By.XPATH)
            password_field.send_keys(password)

            log_append("Clickando no botão submit")
            bot.wait(500)
            submit_button = bot.find_element("//button[contains(@id, 'submit')]", By.XPATH)
            submit_button.click()

            bot.wait(1000)

            try:
                message = bot.find_element('//h1[text()="Logged In Successfully"]', By.XPATH)
                print(message.text)
                log_append("Login sucedido")
                log_append("Finalizando a execução da automação...")
                break
            except:
                log_append("Mensagem de login sucedido não encontrada.")
                count_error += 1

        if count_error == tentativas:
            log_append(f"Foram realizadas {i+1} tentativas de login sem sucesso. Finalizando bot...")

    log_create()
    tentativa_login("student", "Password123", 3)
    bot.wait(2000)
    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues e pull requests para melhorias e correções.
