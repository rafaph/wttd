# Entradas no Banco

[![Build Status](https://travis-ci.org/rafaph/wttd.svg?branch=M2A17_1_Entradas_Banco)](https://travis-ci.org/rafaph/wttd)

## Descrição

Todas as vezes que alguém passa na porta do maior banco da cidade de
Pirenópolis, é gravado em um arquivo de log a data e a hora da
abertura da porta.

Cada registro no arquivo de log possui o seguinte formato:

[YYYY-mm-dd H:i:s] - Abertura da Porta OK

O gerente do banco precisa saber quantas pessoas entraram no banco
no horário de expediente, para isso ele solicitou que você faça um
programa que verifique se o registro de entrada é válido e se a
hora se encontra dentro do intervalo de funcionamento do banco, das
10:00:00 até as 16:00:00.

## Exemplos

### Arquivo de entrada (`log.txt`)

```
2019-11-23 09:59:59 - Abertura da Porta OK
2019-11-23 11:00:00 - Abertura da Porta OK
2019-11-23 16:00:00 - Abertura da Porta OK
2019-11-24 14:00:01 - Abertura da Porta OK
2019-11-24 16:00:01 - Abertura da Porta OK
2019-11-25 08:00:09 - Abertura da Porta OK
```

### Saída esperada

```
> get_people_entered('log.txt')
> 3
```

# Utilização

## Preparação do ambiente

1. Clone o respositório
2. Instale o Python 3.7.* se não o tiver.
3. Altere a branch para `M2A17`.
4. Execute os testes.

```console
git clone git@github.com:rafaph/wttd.git
git checkout -b M2A17
git pull origin M2A17
cd wttd
python -m unittest discover bank_entries
```

## Execução

```
cd bank_entries
python main.py log.txt
```

Observação: O arquivo exemplo utilizado é `log.txt` mas você
pode informar outro arquivo como parâmetro do programa.
