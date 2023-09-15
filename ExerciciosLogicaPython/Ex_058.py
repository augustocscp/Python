import random
from time import sleep
npc = random.randint(0,10)
print('='*55)
print('    ACERTE O NUMERO QUE O PC ESCOLHEU ENTRE 0 E 10.')
print('='*55)
print('Pronto, escolhi o meu número.')
nd = int(input('Sua vez! Digite um número: '))
print('Processando...')
sleep(1)
c = 1
while nd != npc:
    nd = int(input('Errou, Tenta de novo: '))
    print('Processando...')
    sleep(1)
    c += 1
print('Acetou abestado!')
if (c > 1):
    print('Finalmente!')
else:
    print('De primeira, PARABENS!')
