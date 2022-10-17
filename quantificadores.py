import re

texto = '''João trouxe     lindas flores para o seu amor, Maria, no dia 10 de Janeiro de 2022.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente. maria , hoje sua esposa, ainda faz aquele café com pão de queijo às tardes de domingo.
Não canso de ouvir Maria gritar:
"Joooooooãoooooo, o café tá pronto, Veeemmm!!!. jão - jã
'''
# * == 0 ou n vezes
print(re.findall(r'jo*ão*', texto, flags=re.I))
# + == 1 ou n vezes
print(re.findall(r'jo+ão+', texto, flags=re.I))
# ? == 0 ou 1 vez
print(re.findall(r'jo?ão?', texto, flags=re.I))