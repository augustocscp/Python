maispeso = []
maisleve = []
lista_a = list()
lista_b = list()
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista_a.append(nome)
    lista_a.append(peso)
    lista_b.append(lista_a[:])
    if peso > 70:
        maispeso.append(lista_a[:])
    else:
        maisleve.append(lista_a[:])
    lista_a.clear()
    resp = str(input('{}Deseja continuar?[S/N] {}'.format('\033[1:33m','\033[m'))).strip().upper()
    if resp == 'N':
        break
print(f'Foram cadastradas {len(lista_b)} pessoas.')
print(f'As pessoas mais pesadas cadastradas são {maispeso}')
print(f'As pessoas mais leves cadastradas são {maisleve}')




