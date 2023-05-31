# - Elabore um script em linguagem Python que leia de 10 números
# reais, inserindo-os numa lista e ao final, mostre-os na ordem inversa.

numeros = []

for c in range(10):
    numero = float(input('Digite um numeros: '))
    numeros.append(numero)

for n in reversed(numeros):
    print(n)
