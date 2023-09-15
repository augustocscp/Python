cont = int(input('Quantos termos você quer mostrar? '))
na = 0
nb = 1
nc = 0
while cont != 1:
    cont += -1
    print(nc, end='')
    if cont > 1:
        print(' - ', end='')
    else:
        print(' = Fim!', end='')
    nc = na + nb
    na = nb
    nb = nc
