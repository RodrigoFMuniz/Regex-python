import re

texto = '''João trouxe     lindas flores para o seu amor, Maria, no dia 10 de Janeiro de 2022.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria , hoje sua esposa, ainda faz aquele café com pão de queijo às tardes de domingo.
Não canso de ouvir Maria gritar:
"Joooooooãoooooo, o café tá pronto, Veeemmm!!!.
'''

# Metacaractere: | (pipe) -> OU
print(re.findall(r'João|Maria', texto))

# Metacaractere: . (ponto) -> Seleciona quqlaquer caractere, com exceção da quebra de linha.
print(re.findall(r'.oão|Maria|adul..s', texto))



