a = int(input('Digite o valor do lado A: '))
b = int(input('Digite o valor do lado B: '))
c = int(input('Digite o valor do lado C: '))
if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    print('As 3 retas formam um triangulo!')
else:
    print('As 3 retas informadas não podem formar um triangulo!')