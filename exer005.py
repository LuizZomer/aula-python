# Dada uma lista L de n valores inteiros, elabore um programa que remova
# todos os números pares da lista.
# Exemplo:
# Tamanho da lista L: 10
# L:1 2 3 4 5 6 7 8 9 10
# Resposta: 1 3 5 7 9

l = []

while True: 
    numero = int(input('Digite um numero: '))
    l.append(numero)
    continuar = input('Deseja continuar[S/N]: ').upper()
    if continuar == 'N':
        break

l = [n for n in l if n%2!=0]

print(l)