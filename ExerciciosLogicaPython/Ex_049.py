n = int(input('Desejeja a tabuada de qual numero? '))
print('-'*25)
print('   TABUADA DO NÚMERO {}'.format(n))
print('-'*25)
for c in range(1,11):
    print(c, 'x', n, '= ', (c*n))
print('FIM')