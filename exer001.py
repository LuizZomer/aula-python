# Desenvolva um script Python que lê vários números
# positivos via teclado. Quando o número lido for -1, o script
# deve parar e exibir a soma de todos os números positivos
# inseridos, a média desses números, o menor e o maior número
# digitado. No entanto, utilize uma lista para armazenar os
# números.

numeros = []
cont = 0

while True:
    numero = float(input('Digite um numero(-1 para): '))
    if numero == -1:
        break
    numeros.append(numero)
    cont +=1

print(f'O maior numero digitado foi {max(numeros)}\nO menor numero digitado foi {min(numeros)}')
print(f'A soma de todos é {sum(numeros)}\nA média deles é {sum(numeros)/cont}')