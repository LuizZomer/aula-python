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




        





