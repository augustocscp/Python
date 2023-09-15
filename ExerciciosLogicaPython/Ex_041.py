from datetime import datetime

nome = str(input('Qual o nome do atleta? ')).strip()
ano = int(input('Qual o ano de nascimento do atleta?'))
data = datetime.now()
idade = data.year - ano

if (idade < 9.0):
    print('{} está com {} anos e na categoria {}MIRIM{}'.format(nome, idade, '\033[1:34m', '\033[m'))
elif (idade > 9) and (idade < 14.1):
    print('{} está com {} anos e na categoria {}INFANTIL{}'.format(nome, idade, '\033[1:34m', '\033[m'))
elif (idade > 14) and (idade <= 19):
    print('{} está com {} anos e na categoria {}JUNIOR{}'.format(nome, idade, '\033[1:34m', '\033[m'))
elif (idade > 19) and (idade <= 20):
    print('{} está com {} anos e na categoria {}SENIOR{}'.format(nome, idade, '\033[1:34m', '\033[m'))
else:
    print('{} está com {} anos e na categoria {}MASTER{}'.format(nome, idade, '\033[1:34m', '\033[m'))

