from random import randint
from time import sleep
lista_final = []
n_jogos = int(input('Quantos jogos você deseja que eu sorteie? '))
print(f'----------  Sorteando {n_jogos} jogos  ----------')
for c in range(n_jogos):
    lista_provisoria = list((randint(1, 60))for x in range(6))
    lista_provisoria.sort()
    print(f'Jogo {c+1}: {lista_provisoria}')
    lista_final.append(lista_provisoria[:])
    lista_provisoria.clear()
    sleep(1)
print('------------  BOA SORTE!  ------------')
