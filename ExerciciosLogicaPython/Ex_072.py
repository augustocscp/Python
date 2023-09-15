num = int(input('Digite um número entre 0 e 20: '))
n_ext = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    if (num >= 0) and (num <= 20):
        break
    else:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n_ext[num-1]}')