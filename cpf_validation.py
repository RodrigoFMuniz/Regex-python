import re

cpf = '123.456.789-10'

# test_validation = re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf)
test_validation = re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)
# test_validation = re.findall(r'((?:[0-9]{3}[\.-]){3}[0-9]{2})', cpf)

if test_validation:
    print(test_validation)

else:
    print('Errado')