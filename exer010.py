# Elabore um script em linguagem Python que, dados dois inteiros x e y,
# retorna uma lista com todos os valores entre x e y (inclusive), considerando x <
# y. Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]

x = int(input('Inicio: '))
y = int(input('Fim: '))

for c in range(x,y+1):
    print(c)