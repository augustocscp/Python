'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média
de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

nome = list()
medias = list()
maiorSete = int()


for n in range(4):

    #Captação dos dados
    nome.append(str(input('Nome do aluno: ')))

    nota = 0
    mediaprovisoria = 0
    i = 1
    for n in range(4):
        nota = float(input(f'{i}° nota: '))
        mediaprovisoria += nota
        i+=1

    #Calculo de medias
    medias.append(mediaprovisoria / 4)

    #Calculo de notas maiores
    if ((mediaprovisoria / 4) > 7.0):
        maiorSete+= 1

#Demonstração
if maiorSete > 1:
    print(f'{maiorSete} alunos tiveram médias acima de 7.0')
else:
    print(f'{maiorSete} aluno teve média acima de 7.0')