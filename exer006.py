# Dadas duas listas P1 e P2, ambas com n valores reais que representam as
# notas de uma turma na prova 1 e na prova 2, respectivamente. Escreva um
# script em linguagem Python que calcule a média da turma nas provas 1 e 2,
# imprimindo em qual das provas a turma obteve a melhor média. Exemplo:
# Tamanho da turma: 5
# P1: 7.0 8.3 10.0 6.5 9.3 P2: 8.5 6.9 5.0 7.5 9.8
# Resposta:
# Média da turma na prova 1: 8.22
# Média da turma na prova 2: 7.54
# A turma obteve a melhor média na prova 1.

p1 = []
p2 = []


for n in range(10):
    numero = float(input('Digite a nota:'))
    p1.append(numero)

for n in range(10):
    numero = float(input('Digite a nota 2: '))
    p2.append(numero)

media1 = sum(p1)/10
media2 = sum(p2)/10
print('A média 1 foi ',media1)
print('A média 2 foi ',media2)

if media1 > media2:
    print('A média da prova 1 foi maior')
else:
    print('A nota da turma 2 foi maior')