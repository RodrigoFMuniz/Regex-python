import re

# findall - Encontra todas as ocorrências do padrão encontradas no texto
# search - encontra a primeira ocorrência do padrão e seu índice, detro do texto. Retorna um objeto match
# sub - serve para subtituir algo dentro do texto
# compile - serve para compilar regex. Reutilizar regex em alguns casos.


string = "Este é um teste de expressões regulares em python"
print(re.search(r'teste', string))