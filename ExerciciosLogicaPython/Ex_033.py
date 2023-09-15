print('=======================')
print('Qual o maior e o menor?')
print('=======================')
maior = int(0)
menor = int(1)
n1 = int(input('Digite o primeiro número: '))
if (n1 > maior):
    maior = n1
n2 = int(input('Digite o segundo número: '))
if (n2 > maior):
    maior = n2
else:
    menor = n2
n3 = int(input('Digite o terceiro número: '))
if (n3 > maior):
    maior = n3
else:
    if (n3 < menor):
        menor = n3
print('{} é o maior número'.format(maior))
print('{} é o menor número'.format(menor))