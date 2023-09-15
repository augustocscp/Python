nome = str(input('Qual o seu nome? '))
peso = float(input('Qual o peso seu peso {}? '.format(nome)))
alt = float(input('Qual a sua altura {}? '.format(nome)))
imc = peso / (alt**2)
if (imc < 18.5):
    print('{} com IMC de {:.2f}, você é considerado(a) {}ABAIXO DE PESO{}'.format(nome, imc, '\033[1:30:43m', '\033[m'))
elif (imc > 18.5) and (imc <= 25):
    print('{} você está com IMC de {:.2f}! Esse valor indica que você esta no seu {}PESO IDEAL{}'.format(nome, imc, '\033[1:30:42m', '\033[m'))
elif (imc > 25) and (imc <= 30):
    print('{} você está com IMC de {:.2f}! Esse valor indica que você esta com  {}SOBRE PESO{}'.format(nome, imc, '\033[1:30:43m', '\033[m'))
else:
    print('{} você está com IMC de {:.2f}! Esse valor indica que você esta {}ACIMA DO PESO{}'.format(nome, imc, '\033[1:30:43m', '\033[m'))

