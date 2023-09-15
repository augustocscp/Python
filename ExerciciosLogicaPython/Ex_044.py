prod = str(input('Qual produto será comprado? '))
vlr = float(input('Qual o valor do produto? '))
tipo = str(input('Qual a forma de pagamento? \n(1)Dinheiro ou Cheque\n(2)Débito\n(3)Crédito a vista\n(4)Crédito parcecelado '))
if (tipo == '4'):
    cx = int(input('(Deseja dividir em quantas vezes?) '))
if (tipo == '1'):
    print('O valor do {} para pagamento em {} é {}RS {}{}'.format(prod, 'Dinheiro', '\033[0:34m', vlr - (vlr * 0.1), '\033[m'))
elif (tipo == '2') or (tipo == '3'):
    print('O valor do {} para pagamento {} é {}RS {}{}'.format(prod, 'A Vista', '\033[0:34m', vlr - (vlr * 0.05), '\033[m'))
elif (tipo == '4') and (cx == '2'):
    print('O valor do {} para pagamento no {} é {}RS {}{}'.format(prod, 'Credito parcelado 2x', '\033[0:34m', vlr, '\033[m'))
elif (tipo == '4') and (cx > 2):
    print('O valor do {} para pagamento no credito parcelado {}x tem 20% de jutos e fica no valor de {}RS {}{}'.format(prod, 'cx', '\033[0:34m', vlr + (vlr * 0.2), '\033[m'))
else:
    print('Opção de pagamento invalida, tente novamente.')