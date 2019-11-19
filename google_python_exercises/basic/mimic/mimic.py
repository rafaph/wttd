#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

Construa um dicionário "mimic" que mapeia cada palavra que aparece no arquivo
para uma lista com todas as palavras que seguem imediatamente cada palavra no arquivo.
A lista palavras pode estar em qualquer ordem e deve incluir duplicatas. Então, por exemplo
a chave "and" pode ter uma lista de ["then", "best", "then", "after", ...] que lista todas
as palavras que vem depois de "and" no texto.
Digamos que uma string vazia é o que vem antes da primeira palavra no arquivo.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import sys
import random


class MimicDict(object):
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        if item in self.items:
            return self.items[item]
        return self.items[item.lower()]

    def __contains__(self, item):
        if item in self.items:
            return True
        return item.lower() in self.items

    def __setitem__(self, key, value):
        correct_key = key
        if correct_key not in self.items:
            key_lower = key.lower()
            if key_lower in self.items:
                correct_key = key_lower
        self.items[correct_key] = value


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""

    def it_lines(lines_read):
        for line_read in lines_read.split('\n'):
            line_read = line_read.strip()
            if line_read != '':
                yield line_read.split()

    with open(filename) as f:
        lines = f.read()
    result = MimicDict()
    result[''] = []
    for line in it_lines(lines):
        result[''].append(line[0])
        for i, word in enumerate(line[:-1]):
            if word not in result:
                result[word] = []
            result[word].append(line[i + 1])
        if line[-1] not in result:
            result[line[-1]] = ['']

    return result.items


def print_mimic(mimiced_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    next_word = word
    for _ in range(200):
        values = mimiced_dict[next_word] if next_word in mimiced_dict else mimiced_dict[next_word.lower()]
        next_word = random.choice(values)
        end = '\n' if next_word == '' else ' '
        print(next_word, end=end)


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict_result = mimic_dict(sys.argv[1])
    print_mimic(dict_result, '')


if __name__ == '__main__':
    main()
