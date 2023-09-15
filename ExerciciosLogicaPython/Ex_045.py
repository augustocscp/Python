print('-'*20)
print('      Jokempô')
print('-'*20)
nj1 = str(input('Nome do primeiro jogador: '))
nj2 = str(input('Nome do segundo jogador: '))
j1 = str(input('Pedra, papel ou tesoura? '))
j2 = str(input('Pedra, papel ou tesoura? '))
if (j1 == 'pedra') and (j2 == 'tesoura'):
    print('Pedra ganha de Tesoura - {}{} ganhou{}'.format('\033[0:30:42m', nj1, '\033[m'))
elif (j1 == 'pedra') and (j2 == 'papel'):
    print('Pedra perde para Papel - {}{} perdeu{}'.format('\033[0:30:41m', nj2, '\033[m'))
elif(j1 == 'papel') and (j2 == 'pedra'):
    print('Papel ganha de Pedra - {}{} ganhou{}'.format('\033[0:30:42m', nj1, '\033[m'))
elif(j1 == 'papel') and (j2 == 'tesoura'):
    print('Papel perde para Tesoura - {}{} perdeu{}'.format('\033[0:30:41m', nj2, '\033[m'))
elif (j1 == 'tesoura') and (j2 == 'papel'):
    print('Tesoura ganha de papel - {}{} ganhou{}'.format('\033[0:30:42m', nj1, '\033[m'))
else:
    print('Tesoura perde de pedra - {}{} perdeu{}'.format('\033[0:30:41m', nj2, '\033[m'))