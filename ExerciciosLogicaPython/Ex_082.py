lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite o número: ')))
    resp = input('Deseja continuar? [S/N] ').upper().strip()
    print('-'*40)
    if resp == 'N':
        break
for pos, x in enumerate(lista):
    if x % 2 == 0:
        par.insert(pos,x)
    else:
        impar.insert(pos,x)
print('-'*60)
print(f'A lista completa é: {lista}')
print(f'Os valores pares são: {par}')
print(f'Os valores impares são: {impar}')
