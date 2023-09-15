a = int(input('Informe o valor do lado A: '))
b = int(input('Informe o valor do lado B: '))
c = int(input('informe o valor do lado C: '))
if ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((a - b) < c < (a + b)):
    print('As 3 retas formam um triangulo!')
    if (a == b) and (a == c) and (b == c):
        print('E ele é equilatero')
    elif (a != b) and (a != c) and (b != c):
        print('E ele é escaleno')
    else:
        print('E ele é isósceles')
else:
    print('As 3 retas informadas não podem formar um triangulo!')


