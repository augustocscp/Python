'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
n3 = float(input('Digite um numero real: '))
a = n1 * 2 + n2 / 2
print(f'O resultado do produto do dobro do primeiro com metade do segundo é {a}')
b = n1 * 3 + n3
print(f'O resultado da soma do triplo do primeiro com o terceiro {b}')
c = n3 ** 3
print(f'O resultado do terceiro elevado ao cubo é {n3}')