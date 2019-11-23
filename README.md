# Entradas no Banco

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

```console
2019-11-23 09:59:59 - Abertura da Porta OK
2019-11-23 11:00:00 - Abertura da Porta OK
2019-11-23 16:00:00 - Abertura da Porta OK
2019-11-24 14:00:01 - Abertura da Porta OK
2019-11-24 16:00:01 - Abertura da Porta OK
2019-11-25 08:00:09 - Abertura da Porta OK
```

### Saída esperada

```console
> get_people_entered('log.txt', 23)
> 2
> get_people_entered('log.txt', 24)
> 1
> get_people_entered('log.txt', 25)
> 0
```