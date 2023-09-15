id = int(input('Digite a idade: '))
sx = str(input('Digite o sexo [Masculino/Feminino]: ')).strip().upper()
mais18 = homens = mulheres = 0
#ciclo de repetição
while True:
    #verificação das condições impostas na questão
    if (id > 18):
        mais18 += 1
    if (sx == 'MASCULINO'):
        homens += 1
    if (sx == 'FEMININO') and (id < 20):
        mulheres += 1
    #verifiação se deseja continuar ou não
    print('-' * 35)
    resp = str(input('Deseja continuar? ')).strip().upper()
    print('-' * 35)
    if (resp == 'NAO') or (resp == 'NÃO') :
        break
    elif (resp == 'SIM'):
        id = int(input('Digite a idade: '))
        sx = str(input('Digite o sexo [M/F]: ')).strip().upper()
    else:
        print('{}Resposta invalida{}'.format('\033[1:30:41m', '\033[m'))
        resp = str(input('Deseja continuar? ')).strip().upper()
#Tratamento dos dados coletados
print(f'O total de pessoas com 18 anos é {mais18}')
print(f'Ao todo {homens} são homens!')
print(f'E temos {mulheres} mulheres com menos de 20 anos!')
