# Desenvolva um código em Python que adicione em um dicionário “d” os
# seguintes campos: nome, idade, endereço e telefone e mostre os dados no
# final.


d = {}

d['nome'] = input('Nome: ')
d['idade'] = input('Idade: ')
d['endereço'] = input('Endereço: ')
d['telefone'] = input('Telefone: ')

for k,v in d.items():
    print(f'O campo {k} tem o valor {v}')