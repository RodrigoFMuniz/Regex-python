import re

texto = '''
<p>frase 1</p><p>frase 2</p><p>frase 3</p><div>frase 4</div><div></div><div><p>olá</p></div>
'''

print(re.findall(r'<[pdiv]{1,3}>', texto)) # comportamento básico
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto)) # comportamento guloso
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto)) # comportamento lazy
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto)) # comportamento lazy, mas não recupera divs vazias
print(re.findall(r'<[pdiv]{1,3}><[p]+>.+?<\/[p]+><\/[pdiv]{1,3}>', texto)) 
print(re.findall(r'<[pdiv]?>.*?<\/[pdiv]?>', texto)) 