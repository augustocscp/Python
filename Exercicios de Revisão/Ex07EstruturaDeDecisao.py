'Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido'

sexo = str(input("Qual o seu sexo? [F / M]: ")).upper()

if (sexo[0] == 'M'):
    print('Sexo informado: Masculino!')
elif (sexo[0] == 'F'):
    print('Sexo informado: Feminino!')
else:
    print("Sexo informado invalido!")