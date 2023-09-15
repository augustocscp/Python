def leiaInt():
    while True:
        try:
            i = int(input('Digite um número inteiro: '))
        except (NameError,ValueError, TypeError):
            print('{}ERRO! Digite um número inteiro valido{}'.format('\033[0:31m','\033[m'))
        except (KeyboardInterrupt):
            print('{}ERRO! O usuario prefiriu não digitar o número{}'.format('\033[0:31m', '\033[m'))
        else:
            return i

def leiaFloat():
    while True:
        try:
            f = float(input('Digite um número real: '))
            if f == '':
                f = float(0)
        except (NameError,ValueError, TypeError):
            print('{}ERRO! Digite um número real valido{}'.format('\033[0:31m','\033[m'))
        except (KeyboardInterrupt):
            print('{}ERRO! O usuario prefiriu não digitar o número{}'.format('\033[0:31m', '\033[m'))
        else:
            return f

v = leiaInt()
z = leiaFloat()
print(f'O valor inteiro digitado foi {v} e o real {z}')
