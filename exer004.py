# Crie um script em linguagem Python que leia dois vetores com 5
# elementos cada. Gere um terceiro vetor de 10 elementos, cujos
# valores deverão ser compostos pelos elementos intercalados dos dois
# outros vetores. Exibir na tela todos os vetores em linhas separadas.

v1 = []
v2 = []
v3 = []
cont1 = 0
cont2 = 0

for n in range(5):
    ele = input('Adicione algo para v1: ')
    v1.append(ele)

for n in range(5):
    ele = input('Adicione algo para v2: ')
    v2.append(ele)

for n in range(5):
    v3.append(v1[n])
    v3.append(v2[n])

print(v1)
print(v2)
print(v3)