print('-'*35)
print('          LOJINHA DA LIS')
print('-'*35)
total = maisdemil = maisbarato = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if (preço > 1000):
        maisdemil += 1
    if (cont == 0) or (preço < maisbarato):
        cont += 1
        barato = prod
        maisbarato = preço
    resp = str(input('Deseja continuar? ')).strip().upper()
    if (resp == 'NAO') or (resp == 'NÃO'):
        break
    elif (resp == 'SIM'):
        print('-' * 35)
    else:
        print('{}Resposta invalida{}'.format('\033[1:30:41m', '\033[m'))
        resp = str(input('Deseja continuar? ')).strip().upper()
print('-' * 45)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produto custando mais de mil reais')
print(f'O produto mais barato foi {barato} que custa R${maisbarato} reais')
