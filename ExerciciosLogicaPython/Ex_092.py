individual = {}
individual['Nome'] = str(input('Nome: '))
individual['Ano de nascimento'] = int(input('Ano de nascimento: '))
individual['Idade'] = (2023 - individual['Ano de nascimento'])
individual['CTPS'] = int(input('N° da carteira de trabalho: '))
if (individual['CTPS'] > 0):
    individual['Ano de contratação'] = int(input('Qual o ano de contratação? '))
    individual['Salário'] = float(input('Salário: '))
    individual['Aposentadoria'] = (individual['Ano de contratação'] + 35) - individual['Ano de nascimento']
for k,i in individual.items():
    print(f'{k} tem o valor {i}')
