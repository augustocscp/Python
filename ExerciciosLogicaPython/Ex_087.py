matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = []
terceira = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'Digite um número para a [{l} : {c}]: ')))
        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end=' ')
        if c > 1:
            terceira += matriz[l][c]
    if l == 1:
        if maior > 0:
            maior = matriz[l][c]
        elif matriz[l][c] > maior:
            maior = matriz[l][c]
    print()
print(f'Os valores pares digitados são: [{par}]')
print(f'A soma dos valores da 3° coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')