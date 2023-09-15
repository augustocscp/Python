def leiaInt(msg):
    while True:
        valor = 0
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        #else:
        #   print('{}ERRO! Digite um número inteiro válido.{}'.format("\033[0:31m","\033[m"))
    return valor

n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')

"""
while True:
    n = str(input('Digite um número: '))
    if n.isnumeric():
        n = int(n)
        break
    elif (n == ''):
        print('{}ERRO! Digite um número inteiro válido.{}'.format("\033[0:31m","\033[m"))
print(f'Você acabou de digitar o número {n}')"""
