lista = []
while True:
    valores = (int(input('Digite um valor: ')))
    if valores in lista:
        print('{}Esse número ja foi digitado, não posso cadastrar valores repetidos. Tente outro!{}'.format('\033[1:31m', '\033[m'))
    else:
        lista.append(valores)
        print('{}Valor cadastrado!{}'.format('\033[1:34m', '\033[m'))
        resp = str(input('Deseja continuar? [S/N]')).upper().split()
    if resp == ['N']:
        break
lista.sort()
print(f'Os valores digitados foram: {lista}')

