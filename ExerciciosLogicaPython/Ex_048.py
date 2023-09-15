sc = 0
vf = 0
for c in range(3,501,3):
    if (c % 2 != 0):
        sc += 1
        vf += c
        print(c, end=' ')
print('\n','A soma dos {} solicitados é {}'.format(sc, vf))
