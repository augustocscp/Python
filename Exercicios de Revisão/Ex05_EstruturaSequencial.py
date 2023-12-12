'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

area = (float(input('Qual o tamanho da área a ser pintada em m2: ')))
#Calculo litros -> area + 10%
litros = ((area + area * 0.1) / 6)

#Calculo latas
latas = litros // 18
if (litros % 18) != 0:
    latas += + 1

#Calculo galão
galao = litros // 3.6
if (litros % 3.6) != 0:
    galao += 1

#Calculo misto lata
'''if necessario para tratamento de m² inferior ao minimo de 18L'''
mistoLata  = (litros // 18)
if mistoLata < 1:
                mistoLata = 1

#Calculo misto galão
mistoGalao = (litros - mistoLata * 18) // 3.6
if (litros - mistoLata * 18 % 3.6) != 0:
    mistoGalao += 1
if mistoGalao < 0:
    mistoGalao = 0

#Calculo de valor
vlrFinalLata = latas * 80
vlrFinalGalao = galao * 25
vlrFinalMisto = (mistoLata * 20) + (mistoGalao * 25)

#Desmonstração
print('-'*30)
print(f'Para pintar uma medida de {area:,.0f}m², será necessario {litros:,.0f}L de tinta.')
print(f'Para essa quantidade de material você pode optar por levar')
print(f'{latas:,.0f} lata no valor de R$ {vlrFinalLata} reais;')
print(f'{galao:,.0f} galão de tinta a R$ {vlrFinalGalao} reais;')
print(f'{mistoLata:,.0f} lata e {mistoGalao:,.0f} galão! No valor de R$ {vlrFinalMisto} reais')'''
