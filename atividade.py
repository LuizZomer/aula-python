# # Exer 001

# numeros = []
# cont = 0

# while True:
#     numero = float(input('Digite um numero(-1 para): '))
#     if numero == -1:
#         break
#     numeros.append(numero)
#     cont +=1

# print(f'O maior numero digitado foi {max(numeros)}\nO menor numero digitado foi {min(numeros)}')
# print(f'A soma de todos é {sum(numeros)}\nA média deles é {sum(numeros)/cont}')

# exerc 2

# numeros = []

# for c in range(10):
#     numero = float(input('Digite um numeros: '))
#     numeros.append(numero)

# for n in reversed(numeros):
#     print(n)

# exer 3

# alunos = 10
# notas = 4

# todas_notas = []
# media_geral = []

# for a in range(alunos):
#     print(f'Aluno {a+1}')
#     for n in range(notas):
#         nota = float(input(f'Nota {n+1}: '))
#         todas_notas.append(nota)
#         if n == 3:
#             media = sum(todas_notas)/4
#             todas_notas.clear()
#             if media >= 6:
#                 media_geral.append(media)

# print(f'{len(media_geral)} alunos tiraram acima da média')

# exer 4

# v1 = []
# v2 = []
# v3 = []
# cont1 = 0
# cont2 = 0

# for n in range(5):
#     ele = input('Adicione algo para v1: ')
#     v1.append(ele)

# for n in range(5):
#     ele = input('Adicione algo para v2: ')
#     v2.append(ele)

# for n in range(len(v1)+len(v2)):
#     if n%2 == 0:
#         v3.append(v1[cont1])
#         cont1 +=1
#     else:
#         v3.append(v2[cont2])
#         cont2 +=1

# print(v1)
# print(v2)
# print(v3)

# exer 5 

# l = []

# while True: 
#     numero = int(input('Digite um numero: '))
#     l.append(numero)
#     continuar = input('Deseja continuar[S/N]: ').upper()
#     if continuar == 'N':
#         break

# l = [n for n in l if n%2==0]

# print(l)

# exer 6

# p1 = []
# p2 = []


# for n in range(10):
#     numero = float(input('Digite a nota:'))
#     p1.append(numero)

# for n in range(10):
#     numero = float(input('Digite a nota 2: '))
#     p2.append(numero)

# media1 = sum(p1)/10
# media2 = sum(p2)/10
# print('A média 1 foi ',media1)
# print('A média 2 foi ',media2)

# if media1 > media2:
#     print('A média da prova 1 foi maior')
# else:
#     print('A nota da turma 2 foi maior')

# exer 8

# d = {}

# d['nome'] = input('Nome: ')
# d['idade'] = input('Idade: ')
# d['endereço'] = input('Endereço: ')
# d['telefone'] = input('Telefone: ')

# for k,v in d.items():
#     print(f'O campo {k} tem o valor {v}')

# exer 9

# funcionarios= {
#     '0101':'Luiz',
#     '0202':'Jefe',
#     '0303':'Willian',
#     '0404':'Chris',
# }

# while len(funcionarios) > 0:
#     for k,v in funcionarios.items():
#         print(f'Codigo:{k} Funcionario:{v}')

#     demitir = input('Escolha quem você quer demitir: ')

#     print(f'{funcionarios[demitir]} foi demitido')
#     funcionarios.pop(demitir)

# print('Todos foram demitidos')

# exer 10

# x = int(input('Inicio: '))
# y = int(input('Fim: '))

# for c in range(x,y+1):
#     print(c)

# exer 11

l1 = []
l2 = []
l3 = []
cont = 0

for c in range(3):
    x = int(input('Numeros para lista 1: '))
    l1.append(x)
for c in range(3):
    y = int(input('Numeros para lista 2: '))
    l2.append(y)

for r in range(3):
    l3.append(l1[cont] + l2[cont])
    cont+=1

print(l1)
print(l2)
print(l3)






