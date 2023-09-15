dados = dict()
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input(f'Media de {dados["nome"]}: '))
if dados['media'] < 7.0:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Aprovado'
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'Situação é igual a {dados["situação"]}')