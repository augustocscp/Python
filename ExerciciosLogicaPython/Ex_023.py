import math
num = int(input('Digite um número: '))
m = num // 1000 % 100
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))

#Forma simplista de fazer o código, so funciona com 4 digitos.
'''print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))'''
