from datetime import datetime

# Função para criação de log
def log_create():
    global nome_arquivo_log
    # Obter a data e hora atuais
    datetime_atual = datetime.now()

    # Formatar a data para nome do log
    data_hora_formatada = datetime_atual.strftime("%d-%m-%y_%H-%M-%S")

    # Salvar o nome do arquivo de log
    nome_arquivo_log = f"logs/{data_hora_formatada}.txt"

    # Cria log com datetime como nome do arquivo
    log = open(nome_arquivo_log, "a")
    log.close()  # Fechar o arquivo após a criação

# Função para append no log
def log_append(message):
    global nome_arquivo_log
    # Formatar datetime para timestamp no log
    datetime_stamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

    # Mensagem de log com timestamp
    mensagem = f"({datetime_stamp}) - {message}"

    # Adicionar a mensagem ao log
    with open(nome_arquivo_log, "a") as log:
        log.write(mensagem + '\n')