import random
from random import randint
from time import sleep
lista = []


def contador(x):
    c = 0
    print('Analisando os valores passados...')
    while (c < x):
        n = random.randint(0, 10)
        print(n, end=' ')
        sleep(0.3)
        c += 1
        lista.append(n)
    print(f'- Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi o {max(lista)}')
    print('-'*50)
    lista.clear()

print('-' * 50)
contador(6)
contador(3)
contador(2)
contador(1)


