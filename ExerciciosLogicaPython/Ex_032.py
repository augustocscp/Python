print('================================')
print('          Ano Bicesto?          ')
print('================================')
ano = int(input('Qual ano deseja consultar? '))
if (ano % 4 == 0):
    print('O ano {} é BISSEXTO! '.format(ano))
else:
    print('O ano {} não é BISSExTO!'.format(ano))