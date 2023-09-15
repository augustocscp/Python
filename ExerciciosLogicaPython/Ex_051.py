print('='*26)
print('   10 TERMOS DE UMA PA')
print('='*26)
pt = int(input('Primeiro termo: '))
r = int(input('razão: '))
for c in range(0,10):
    print(pt, ' - ', end='')
    pt += r
print('ACABOU!')