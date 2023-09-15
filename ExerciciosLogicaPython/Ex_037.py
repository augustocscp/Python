n = int(input('Digite um número: '))
b = int(input('Em qual base de conversão deseja visualizar? \n'
      '[1]Binario\n'
      '[2]Octal\n'
      '[3]Hexadecimal\n'
      'Sua opção:'))
if (b == 1):
    print('O numero decimal {} em Binario fica {}'.format(n, bin(n)[2:]))#converção de decimal para binario
elif (b == 2):
    print('O numero decimal {} em Octa fica {}'.format(n, oct(n)[2:]))#converção de decimal para octal
else:#converção de decimal para hexadecimal
    print('O numero decimal {} em Hexadecimal fica {}'.format(n, hex(n)[2:]))#conversão para hexadecimal

