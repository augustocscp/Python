'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area = (float(input('Qual o tamanho da área a ser pintada em m2: ')))
litros = area / 3
latas = litros // 18
if (litros % 18) != 0:
    latas += + 1
vlrFinal = latas * 80
print(f'Será necessario {litros} de tinta. ')
print(f'Para essa qtd de litros, você deverá levar {latas} de tinta. Totalizando R$:{vlrFinal}')
