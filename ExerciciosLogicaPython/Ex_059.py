v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
esc = str(1)
while esc != '5':
    esc = str(input('O que deseja fazer agora?\n'
          '[1]Somar\n'
          '[2]Multiplicar\n'
          '[3]Maior\n'
          '[4]Novos numeros\n'
          '[5]Sair do programa\n'
    '-----> Qual a sua escolha? '))
    if esc == '1':
        print('{}A soma de {} + {} = {}{}'.format('\033[1:34m', v1, v2, (v1+v2),'\033[m'))
    elif esc == '2':
        print('{}A multiplicação de {} X {} = {}{}'.format('\033[1:34m', v1, v2, (v1*v2), '\033[m'))
    elif esc == '3':
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('{}{} é o maior valor digitado!{}'.format('\033[1:34m', maior, '\033[m'))
    elif esc == '4':
        v1 = str(input('{}Digite um novo primeiro valor: {}'.format('\033[1:34m', '\033[m')))
        v2 = str(input('{}Digite um novo segundo valor: {}'.format('\033[1:34m', '\033[m')))
