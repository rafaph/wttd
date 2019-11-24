# Jokenpo

## Descrição

Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:

* Pedra empata com Pedra e ganha de Tesoura
* Tesoura empata com Tesoura e ganha de Papel
* Papel empata com Papel e ganha de Pedra

## Exemplo

```
> jokenpo('pedra', 'papel')
Jogador 2

> jokenpo('pedra', 'tesoura')
Jogador 1

> jokenpo('tesoura', 'papel')
Jogador 1

> jokenpo('pedra', 'pedra')
Empate

```

## main.py

```console
python main.py pedra papel
Jogador 2

```