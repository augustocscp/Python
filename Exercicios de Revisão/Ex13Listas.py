'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

numeros = (1,5,6,7,9)

for num in numeros:
    print(num, end=' ')
print()

print('-' * 85)
#-----------------------------------------------#-----------------------------------------------#
'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''


num = list()
i = 1

for a in range (0,10):
    num.append(float(input(f'Digite o {i} números: ')))
    i += 1

print(f'Numeros digitadis: {num}')
#-----------------------------------------------#-----------------------------------------------#
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
#-----------------------------------------------#-----------------------------------------------#
'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média 
anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,...).'''

mes = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
temperaturas = []

temp2023 = 0
tempMedia = 0

#Captação de informações
for i in range(12):
    provisorio = float(input(f'Informe a temperatura do {i+1}° mês : '))
    temperaturas.append(provisorio)
    temp2023 += provisorio

#Calculo da média
tempMedia = temp2023 / 12

#Retorno
print(f'A temperatura média do ano foi de {tempMedia:.1f}°')
print()
for i in range(12):
    if (temperaturas[i] > tempMedia):
        print(f'{mes[i]} - {temperaturas[i]:.1f}°')

















































