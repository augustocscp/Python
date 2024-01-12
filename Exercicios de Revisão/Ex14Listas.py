'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''


num = list()
i = 1

for a in range (0,10):
    num.append(float(input(f'Digite o {i} números: ')))
    i += 1

print(f'Numeros digitadis: {num}')