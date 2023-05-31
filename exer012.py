# Desenvolva um script em linguagem Python, utilizando Dicionários, que
# solicite ao usuário inserir o nome de três produtos de mercado e seus
# respectivos preços e os mostre na tela.

produtos = []


for c in range(3):
    produto = {}
    produto['nome'] = input(f'Digite o nome do produto {c+1}: ')
    produto['preço'] = input(f'Digite o preço do produto {c+1}: ')
    produtos.append(produto)

for p in produtos:
    print(f'O produto {p["nome"]} Tem o preço: {p["preço"]}')
        
