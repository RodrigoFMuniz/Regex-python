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

## re.findall

- Encontra todas as ocorrências do padrão encontradas no texto
- Retorna uma lista

        string = "Este é um teste de expressões regulares em python, outro teste"
        print(re.findall(r'teste', string))
        # retorna `['teste', 'teste']`

## re.sub

- Serve para subtituir algo dentro do texto

        string = "Este é um teste de expressões regulares em python, outro teste"
        print(re.sub(r'teste','Olá Mundo', string)

        #retorna `Este é um Olá Mundo de expressões regulares em python, outro Olá Mundo`

        #Usando o param count=1 fica assim.
        print(re.sub(r'teste','Olá Mundo', string, count=1))

        # retorna `Este é um Olá Mundo de expressões regulares em python, outro teste`
