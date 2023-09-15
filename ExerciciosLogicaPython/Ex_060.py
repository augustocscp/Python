n = int(input('Digite um número que deseja calcular o fatorial: '))
print('Calculando o {}! = {}'.format(n, n), end='')
res = 1
while n != 1:
    res *= n
    n += -1
    print(' x', n, end='')
print(' = {}'.format(res))
