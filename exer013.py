#  Desenvolver um programa que leia a altura de 15 pessoas. Este programa
# deverá calcular e mostrar:
# a. A menor altura do grupo;
# b. A maior altura do grupo;
# c. Em uma lista cada um dos dados de entrada.

altura = []

for c in range(5):
    a = float(input(f'Digite a altura da pessoa {c+1}: '))
    altura.append(a)

print(f'A maior altura registrada foi {max(altura)}')
print(f'A menor altura registrada foi {min(altura)}')
print(f'Todas as alturas registradas foram {altura}')

