import random

nr = random.choice([1,2,3,4,5])
print('======================================')
print('ACERTE O NUMERO QUE A MAQUINA ESCOLHEU')
print('======================================')
nd = int(input('Digite um numero: '))
if  nr == nd:
    print('Acetou mizeravel!!!')
else:
    print('Errou miséria, tente de novo!')
