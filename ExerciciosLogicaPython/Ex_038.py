n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
if (n1 == n2):
    print('Os valores digitados são iguais {} - {}'.format(n1, n2))
elif (n1 > n2):
    print('O primeiro valor ({}) é maior que o segundo ({})'.format(n1, n2))
else:
    print('O segundo valor ({}) é maior que o primeiro ({})'.format(n2, n1))
