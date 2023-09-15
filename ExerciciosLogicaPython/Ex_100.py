import random
from random import randint

gerados = []
def sorteio(x):
    for c in range(0,x):
        n = random.randint(1,9)
        gerados.append(n)
    print(f'Sorteando {x} valores da lista: {gerados} PRONTO!', end=' ')

def soma():
    par = 0
    for x,y in enumerate(gerados):
        if y % 2 == 0:
            par += y
    print(f'\nSomando os valores pares de {gerados}, temos {par}')


sorteio(6)
soma()

