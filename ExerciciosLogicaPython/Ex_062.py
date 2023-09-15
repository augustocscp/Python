print('='*26)
print('     TERMOS DE UMA PA')
print('='*26)
pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c1 = 10
c2 = 1
cont = 0
while c2 != 0:
    cont += c1
    while c1 != 0:
        print(pt, ' - ', end='')
        pt += r
        c1 += -1
    print('PAUSA')
    c2 = int(input('Quantos termos você quer mostrar a mais? '))
    c1 = c2
print('Progressão finalizada com {} termos mostrados.'.format(cont))
