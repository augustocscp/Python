lista_final = list()
par = []
impar = []
c = 0
while c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
        par.sort()
    else:
        impar.append(valor)
        impar.sort()
lista_final.append(par)
lista_final.append(impar)
print(f'Os valors impares digitados são: {impar}')
print(f'Os valores pares informados foram: {par}')
