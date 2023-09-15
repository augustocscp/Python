while True:
    m = c = 0
    n = int(input('Quer ver a tabuada de que número? '))
    print('-' * 35)
    if  (n < 0):
        break
    else:
        for c in range(0, 10):
            m += 1
            print(f'{n} x {m} = {n * m}')
    print('-' * 35)
    print('\nCaso queira sair, basta digitar um numero negativo.')
print('{}Programa de tabuada encerrado. Volte sempre!{}'.format('\033[1:34m', '\033[m'))