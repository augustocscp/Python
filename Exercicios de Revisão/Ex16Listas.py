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
