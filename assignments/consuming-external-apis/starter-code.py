# Código Inicial: Consuming External APIs with Python
#
# Instale as dependências:  pip install -r requirements.txt
# Rode o programa:          python starter-code.py
#
# A API Open-Meteo é gratuita e não exige chave de acesso.

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10


# Tarefa 1: faça a requisição de geocodificação e retorne (latitude, longitude, nome)
# Tarefa 2: trate Timeout, HTTPError e RequestException, retornando None em caso de falha
def buscar_coordenadas(cidade):
    pass


# Tarefa 2 e 3: consulte a previsão diária e retorne o JSON da resposta
# Parâmetros necessários: latitude, longitude, timezone=auto e
# daily=temperature_2m_max,temperature_2m_min,precipitation_sum
def buscar_previsao(latitude, longitude):
    pass


# Tarefa 3: converta as listas paralelas de dados["daily"] em uma lista de dicionários
# com as chaves: data, temp_max, temp_min, chuva
def extrair_dias(dados):
    pass


# Tarefa 4: imprima a tabela de dias e as estatísticas do período
def exibir_relatorio(nome_cidade, dias):
    pass


# Tarefa 4: repita o fluxo até o usuário escolher sair
def main():
    cidade = input("Digite o nome da cidade: ")
    print(cidade)


if __name__ == "__main__":
    main()
