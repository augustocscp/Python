num = int(input('Digite um número: '))
s = 0
for c in range(1,101-(100-num)):
    if num % (c) == 0:
        print('\033[0:32m', end='')
        s += 1
    else:
        print('\033[0:31m', end='')
    print('{} '.format(c), end='')
print('\033[m', '\n')
if (s == 2):
    print('O número {} foi divisivel {} vezes!'.format(num, s))
    print('E por isso ele é PRIMO!')
else:
    print('O número {} foi divisivel {} vezes!'.format(num, s))
    print('E por isso ele é NÃO É PRIMO!')