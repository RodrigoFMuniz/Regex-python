import re

# search - encontra a primeira ocorrência do padrão e seu índice, detro do texto. Retorna um objeto match, ou None
string = "Este é um teste de expressões regulares em python, outro teste"
print(re.search(r'teste', string)) # retorna um objeto match, ou None

# findall - Encontra todas as ocorrências do padrão encontradas no texto
print(re.findall(r'teste', string)) # retorna uma lista

# sub - serve para subtituir algo dentro do texto
print(re.sub(r'teste','Olá Mundo', string)) 
print(re.sub(r'teste','Olá Mundo', string, count=1)) 

# compile - serve para compilar regex. Reutilizar regex em alguns casos.
regex = re.compile(r'teste')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub("def", string))