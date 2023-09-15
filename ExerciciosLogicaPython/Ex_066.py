s = nd = 0
while True:
    n = int(input('Digite um numero ou [999 para parar]: '))
    if n == int(999):
        break
    else:
        nd += 1
        s += n
print(f'A soma dos {nd} digitador é {s:.2f}')