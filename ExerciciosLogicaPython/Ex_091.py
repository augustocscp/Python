from random import randint
from time import sleep
dados = {}
c = 1
#GERAÇÃO DOS DADOS
print('-'*50)
print('{:^50}'.format('SORTEIO'))
print('-'*50)
for n in range(1,5):
    dados[n] = randint(0,6)#GERAÇÃO DOS NUMEROS ALEATORIOS
    print(f'O jogador {n} tirou {dados[n]}')
    sleep(0.5)
#GERAÇÃO DO RESULTADO
print('-'*50)
print('{:^50}'.format('RESULTADO'))
print('-'*50)
#ESTUTURA PARA ORDENAR A LISTA
for n in sorted(dados, key = dados.get, reverse=True):
    print(f'{c}° Lugar: Jogador n°{n} com {dados[n]}')
    sleep(0.5)
    c += 1