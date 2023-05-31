# – Elabore um script em linguagem Python, utilizando Dicionários, que
# contenha 4 funcionários, com o índice numérico e seu nome. Em seguida,
# solicite do usuário demitir um dos funcionários conforme o número de
# cadastro e mostre na tela os funcionários restantes.

funcionarios= {
    '0101':'Luiz',
    '0202':'Jefe',
    '0303':'Willian',
    '0404':'Chris',
}

while len(funcionarios) > 0:
    for k,v in funcionarios.items():
        print(f'Codigo:{k} Funcionario:{v}')

    demitir = input('Escolha quem você quer demitir: ')

    print(f'{funcionarios[demitir]} foi demitido')
    funcionarios.pop(demitir)

print('Todos foram demitidos')