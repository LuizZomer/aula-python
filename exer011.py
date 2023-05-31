# Em um script Python com duas listas de três elementos com números
# inteiros, crie uma nova lista onde cada elemento é a soma dos elementos de
# mesma posição nas duas primeiras listas.
# Exemplo: Lista1 = [1, 4, 6] Lista2 = [2, 4, 3] Lista_resultante = [3, 8, 9]


l1 = []
l2 = []
l3 = []

for c in range(3):
    x = int(input('Numeros para lista 1: '))
    l1.append(x)
for c in range(3):
    y = int(input('Numeros para lista 2: '))
    l2.append(y)

for r in range(3):
    l3.append(l1[r] + l2[r])

print(l1)
print(l2)
print(l3)