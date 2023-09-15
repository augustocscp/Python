posmin = list ()
posmax = list ()
valores = list(int(input(f'Digite um valor para a posição {c}: ')) for c in range(5))
for posiçao, v in enumerate(valores):
    if v == min(valores):
        posmin.append(posiçao)
    elif v == max(valores):
        posmax.append(posiçao)
print(f'Os valores digitados foram {valores}')
print(f'O maior número digitado foi {max(valores)}. Ele está nas posições {posmax}')
print(f'O menor número digitado foi {min(valores)}. Ele está nas posições {posmin}')
