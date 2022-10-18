import re

texto = '''
<p>frase 1</p><p>frase 2</p><p>frase 3</p><div>frase 4</div>
'''

print(re.findall(r'<[pdiv]{1,3}>', texto)) # comportamento básico
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]>', texto)) # comportamento guloso