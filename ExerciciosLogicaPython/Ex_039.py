nasc = int(input('Qual o seu ano de nascimento? '))
if (2023 - nasc) == 18:
    print('Está na hora de se alistar para o serviço militar obrigatorio')
elif (2023 - nasc) < 18:
    print('Você ainda não precisa se alistar no serviço militar obrigatorio.')
else:
    print('{} Você está atrasado com o alistamento obrigatorio. Regularise essa pendência {}.'.format('\033[1:30:41m','\033[m'))