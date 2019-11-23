# Eventex

[![Build Status](https://travis-ci.org/rafaph/wttd.svg?branch=master)](https://travis-ci.org/rafaph/wttd)
[![Maintainability](https://api.codeclimate.com/v1/badges/2122878c1dd884763c6c/maintainability)](https://codeclimate.com/github/rafaph/wttd/maintainability)

Sistema de Eventos encomendado pela Morena

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.7.*
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:rafaph/wttd.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de e-mail.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configurar o e-mail aqui
git push heroku master --force
```