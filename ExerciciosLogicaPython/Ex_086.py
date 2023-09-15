a = []
b = []
c = []
i = 0
while i in range(0,9):
    valor = (int(input(f'Digite um valor para : ')))
    i += 1
    if i <= 3:
        a.append(valor)
    elif i > 3 and i < 7:
        b.append(valor)
    elif i > 6:
        c.append(valor)
print(a)
print(b)
print(c)