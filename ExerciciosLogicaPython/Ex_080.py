lista = []
for c in range(0,6):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        for pos, v in enumerate(lista):
            if valor <= v:
                lista.insert(pos,valor)
                break
print(f'Os valores digitados em ordem, foram: {lista}')
