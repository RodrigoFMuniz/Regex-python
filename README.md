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

## re.compile

- Serve para compilar regex.
- Reutilizar regex em alguns casos.

        string = "Este é um teste de expressões regulares em python, outro teste"
        regex = re.compile(r'teste')
        print(regex.search(string))
        print(regex.findall(string))
        print(regex.sub("def", string))

## Metacaracteres

- São caracteres especiais, que possuem outros significados dentro de regex.
- Para escapá-los é necessário usa o '\' antes do metacaractere

        import re

        texto = '''João trouxe     lindas flores para o seu amor, Maria, no dia 10 de Janeiro de 2022.

        Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria , hoje sua esposa, ainda faz aquele café com pão de queijo às tardes de domingo.
        Não canso de ouvir Maria gritar:
        "Joooooooãoooooo, o café tá pronto, Veeemmm!!!.
        '''

        # Metacaractere: | (pipe) -> OU
        print(re.findall(r'João|Maria', texto))

        # retorna ['João', 'Maria', 'Maria']


        # Metacaractere: . (ponto) -> Seleciona quqlaquer caractere, com exceção da quebra de linha.
        print(re.findall(r'.oão|Maria|adul..s', texto))

        # retorna ['João', 'Maria', 'joão', 'adultos', 'Maria', 'ooão']
