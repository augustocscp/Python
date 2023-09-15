nome = str(input('Qual o nome do aluno? '))
n1 = int(input('Digite a nota A1 de {}: '.format(nome)))
n2 = int(input('Digite a nota A2 de {}: '.format(nome)))
media = (n1 + n2) / 2
if (media < 5.0):
    print('O aluno {} tirou média ({}) abaixo do minimo e por isso está {}REPROVADO{}! '.format(nome, media, '\033[1:30:41m', '\033[m'))
elif (media >= 5.0) and (media <= 6.9):
    print('O aluno {} ficou com média {}, abaixo do necessario para passar direto e por isso está de {}RECUPERAÇÃO{}!'.format(nome, media, '\033[1:30:44m', '\033[m'))
else:
    print ('Parabens {}! Sua média ({}) foi acima do necessario e por isso você foi {}APROVADO{}!'.format(nome, media, '\033[1:30:42m','\033[m'))