# Desenvolva um script em linguagem Python que peça as quatro
# notas de 10 alunos, calcule e armazene num vetor a média de cada
# aluno, imprima o número de alunos com média maior ou igual a 7.

alunos = 10
notas = 4

todas_notas = []
media_geral = []

for a in range(alunos):
    print(f'Aluno {a+1}')
    for n in range(notas):
        nota = float(input(f'Nota {n+1}: '))
        todas_notas.append(nota)
        if n == 3:
            media = sum(todas_notas)/4
            todas_notas.clear()
            if media >= 6:
                media_geral.append(media)

print(f'{len(media_geral)} alunos tiraram acima da média')