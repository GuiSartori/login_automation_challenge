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

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues e pull requests para melhorias e correções.
