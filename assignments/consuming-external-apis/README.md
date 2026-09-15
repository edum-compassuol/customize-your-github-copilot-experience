# 📘 Assignment: Consuming External APIs with Python

## 🎯 Objective

Você vai aprender a consumir APIs públicas em Python com a biblioteca `requests`, tratando parâmetros de consulta, códigos de status HTTP, falhas de rede e respostas JSON aninhadas. Ao final, você terá um programa que busca dados meteorológicos reais e gera um pequeno relatório.

## 📝 Tasks

### 🛠️ Primeira Requisição HTTP

#### Descrição

Use a API pública [Open-Meteo](https://open-meteo.com/) (não exige chave de acesso) para descobrir as coordenadas de uma cidade informada pelo usuário. A rota de geocodificação é `https://geocoding-api.open-meteo.com/v1/search` e aceita os parâmetros `name`, `count` e `language`.

#### Requisitos

O programa concluído deve:

- Implementar a função `buscar_coordenadas(cidade)` usando `requests.get()` com os parâmetros passados via argumento `params` (nunca concatenados na string da URL)
- Retornar uma tupla `(latitude, longitude, nome_encontrado)` quando a cidade existir
- Retornar `None` quando a API responder com a chave `results` ausente ou vazia
- Imprimir as coordenadas encontradas no console

Exemplo de saída:

```
Cidade: Curitiba (BR)
Coordenadas: -25.4278, -49.27305
```

### 🛠️ Tratamento de Erros e Timeouts

#### Descrição

Uma chamada de rede pode falhar de várias formas: o servidor pode demorar, cair, ou responder com um código de erro. Torne suas requisições resilientes para que o programa nunca quebre com um traceback.

#### Requisitos

O programa concluído deve:

- Passar `timeout=10` em todas as chamadas de rede
- Chamar `response.raise_for_status()` para transformar respostas 4xx e 5xx em exceções
- Capturar `requests.exceptions.Timeout`, `requests.exceptions.HTTPError` e `requests.exceptions.RequestException` com mensagens distintas e amigáveis para cada caso
- Retornar `None` em vez de propagar a exceção, permitindo que o programa continue rodando
- Nunca encerrar com um traceback não tratado, mesmo se a cidade não existir ou a internet estiver indisponível

Exemplo de saída em caso de falha:

```
Erro: a requisição demorou mais de 10 segundos. Tente novamente.
```

### 🛠️ Parse de JSON Aninhado

#### Descrição

Com as coordenadas em mãos, consulte a previsão do tempo em `https://api.open-meteo.com/v1/forecast`, passando `latitude`, `longitude`, `daily=temperature_2m_max,temperature_2m_min,precipitation_sum` e `timezone=auto`. A resposta traz listas paralelas dentro da chave `daily`, que você precisa combinar em uma estrutura mais fácil de usar.

#### Requisitos

O programa concluído deve:

- Implementar a função `buscar_previsao(latitude, longitude)` que retorna o JSON da previsão
- Implementar a função `extrair_dias(dados)` que converte as listas paralelas em uma lista de dicionários com as chaves `data`, `temp_max`, `temp_min` e `chuva`
- Usar `zip()` para percorrer as listas paralelas simultaneamente
- Usar `dict.get()` com valores padrão ao acessar chaves que podem não existir na resposta
- Retornar uma lista vazia se a chave `daily` não estiver presente

Exemplo do resultado de `extrair_dias`:

```python
[
    {"data": "2026-09-15", "temp_max": 24.3, "temp_min": 13.1, "chuva": 0.0},
    {"data": "2026-09-16", "temp_max": 21.7, "temp_min": 14.8, "chuva": 5.2},
]
```

### 🛠️ Relatório Agregado

#### Descrição

Transforme os dados coletados em um relatório legível no console, com estatísticas calculadas a partir da previsão dos próximos dias.

#### Requisitos

O programa concluído deve:

- Imprimir uma tabela com uma linha por dia contendo data, temperatura mínima, máxima e precipitação
- Formatar todas as temperaturas com uma casa decimal
- Calcular e exibir a temperatura média máxima do período
- Identificar e exibir o dia mais quente e o dia mais chuvoso
- Exibir a contagem de dias com previsão de chuva (precipitação maior que zero)
- Perguntar ao usuário se deseja consultar outra cidade e repetir o fluxo até que ele escolha sair

Exemplo de saída:

```
Previsão para Curitiba (BR) — próximos 7 dias

Data          Mín     Máx    Chuva
2026-09-15   13.1    24.3     0.0 mm
2026-09-16   14.8    21.7     5.2 mm

Temperatura máxima média: 23.0 °C
Dia mais quente: 2026-09-15 (24.3 °C)
Dia mais chuvoso: 2026-09-16 (5.2 mm)
Dias com chuva: 1 de 7

Consultar outra cidade? (s/n)
```
