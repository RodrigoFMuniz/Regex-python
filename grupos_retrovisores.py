import re 

texto = '''
<p>frase 1</p><p>frase 2</p><p>frase 3</p><div>frase 4</div><div></div><div><p>olá</p></div>
'''

# Grupos

print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>', texto))
print(re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)', texto))
print(re.findall(r'<([pdiv]{1,3})>(.*?)<\/\1>', texto))
# tags = re.findall(r'<([pdiv]{1,3})>(.*?)<\/\1>', texto)
tags = re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>', texto)
print(tags)

# for t in tags:
#     um, dois, tres = t
#     # if tres == '':
#     #     tres = 'vazio'
#     print(tres)