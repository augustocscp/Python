import random
print('-' * 35)
print('           PAR ou IMPAR')
print('-' * 35)
vitorias = empates = 0
while True:
#gerando o numero e o par ou impar do computador
    pcn = random.randint(0, 10)
    pcpir = random.randint(0, 1)
#convertendo o numero para str
    if pcpir == 0:
        pcpi = 'PAR'
    else:
        pcpi = 'IMPAR'
#Solicitação para o usuario escolher número e par ou impar
    un = int(input('Escolha um numero: '))
    upi = str(input('Escola PAR ou IMPAR: ')).upper().strip()
#Validando se a soma é par ou impar
    if (un + pcn) % 2 == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'IMPAR'
#Validação do ganhador e condição de encerramento do While
    if (parouimpar == pcpi) and (parouimpar != upi):
        print('{}A MAQUINA GANHOU!{}'.format('\033[1:31m', '\033[m'))
        print(f'Jogo encerrado! O usuario ganhou {vitorias} vezes, empatou {empates} e perdeu 1')
        break
    elif (parouimpar == upi) and (parouimpar != pcpi):
        print('{}HUMANO GANHOU{}'.format('\033[1:34m', '\033[m'))
        vitorias += 1
    elif (parouimpar == upi) and (parouimpar == pcpi):
        print('{}EMPATE, tentem novamente!{}'.format('\033[1:33m', '\033[m'))
        empates += 1
    print('-' * 35)