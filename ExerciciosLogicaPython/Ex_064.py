cont = soma = quant = 0
while cont != 999:
    num = int(input('Digite um numero: '))
    cont = num
    quant += 1
    soma += num
soma += -999
print('Foram digitados {} e a soma deles é {}'.format(quant, soma))
