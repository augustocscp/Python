print('='*26)
print('   10 TERMOS DE UMA PA')
print('='*26)
pt = int(input('Primeiro termo: '))
r = int(input('razão: '))
c = 10
while c != 0:
    print(pt, ' - ', end='')
    pt += r
    c += -1
print('ACABOU!')