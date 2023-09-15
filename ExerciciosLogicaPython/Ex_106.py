cores = {'branco': '\033[0::40m',
         'azul': '\033[0:30:46m',
         'vermelho': '\033[0:30:41m',
         'amarela': '\033[0:30:43m',
         'limpa': '\033[m',
         'roxo': '\033[0:30:45m'}

def com(msg):
    from time import sleep
    print('{}'.format(cores['azul']), '-'*(len('Acessando a biblioteca')+len(msg)+5))
    print('{}  Acessando a biblioteca {}   '.format(cores['azul'],msg))
    print('{}'.format(cores['azul']), '-'*(len('Acessando a biblioteca')+len(msg)+5))
    sleep(1)
    print('{}'.format(cores['branco']))
    help(msg)
    print('{}'.format(cores['limpa']), end='')
    return com


retorno = ''
while True:
    print('{}'.format('\033[0::43m'), '-' * len('  SISTEMA DE AJUDA PyHELP  '))
    print('  SISTEMA DE AJUDA PyHELP  ')
    print('-' * len('  SISTEMA DE AJUDA PyHELP  '))
    print('{}'.format('\033[m'),end='')
    retorno = str(input('Função ou Biblioteca: '))
    if (retorno == 'fim'):
        break
    else:
        com(retorno)
print('{}Ate logo'.format(cores['roxo']))

------------------------------------------------------------------------------------------------------------------------
#SEGUNDA FORMA DE FAZER

#SISTEA DE CORES.-:
cores = {'branco': '\033[7:40m',
         'azul': '\033[0:30:46m',
         'vermelho': '\033[0:30:41m',
         'amarela': '\033[0:30:43m',
         'limpa': '\033[m',
         'roxo': '\033[0:30:45m'}

def titulo(tit,cor=0):
    tam = len(tit) + 4
    print(cores[cor],end='')
    print('-'*tam)
    print(tit)
    print('-'*tam)
    print(cores['limpa'],end='')


def com(msg):
    from time import sleep
    titulo('  Acessando biblioteca', 'amarela')
    sleep(1)
    print(cores['branco'], end='')
    help(msg)
    print(cores['limpa'], end='')
    return com


#PROGRAMA PRINCIPAL
retorno = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 'azul')
    retorno = str(input('Função ou Biblioteca: '))
    if (retorno == 'fim'):
        break
    else:
        com(retorno)
print('{}Ate logo'.format(cores['roxo']))
