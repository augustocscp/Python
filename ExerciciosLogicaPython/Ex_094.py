lista = []
ind = {}
mulher = []
total = idade = 0
while True:
    ind.clear()
    total += 1
    ind['Nome'] = str(input('Nome: '))
    while True:
        ind['Sexo'] = str(input('Sexo[M/F]: ')).upper()
        if ind['Sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F')
    if ind['Sexo'] == 'F':
        mulher.append(ind['Nome'])
    ind['Idade'] = int(input('Idade: '))
    idade += ind['Idade']
    lista.append(ind.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if (resp == 'N'):
        break
media = idade / total
print('-'*50)
print('{:^50}'.format('RESULTADO'))
print('-'*50)
print(ind)
print(lista)

print(f'O grupo tem {total} pessoas.')
print(f'A média de idade é de {media} anos.')
print(f'As mulheres cadastradas foram {mulher}.')
print('Lista das pessoas que estão acima da média de idade: ')
for n in lista:
    if n['Idade'] >= media:
        for k, v in n.items():
            print(f'{k} = {v}',end='')
        print()
