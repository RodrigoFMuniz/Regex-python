# Regex

## Conceito

- É uma forma flexível de identificar cadeias de caracteres que contenham determinados padrões dentro de strings.

## Módulo re

`import re`

## Padrão de utilização

re.método(r'padrão', texto_a_ser_escaneado)

## re.search

- Retorna um objeto Match, com a posição da primeira ocorrência do padrão
- Retorna None

        string = "Este é um teste de expressões regulares em python, outro teste"
        print(re.search(r'teste', string))

        #retorna `<re.Match object; span=(10, 15), match='teste'>`
