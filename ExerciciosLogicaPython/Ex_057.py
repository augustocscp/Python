sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while (sexo != 'M') and (sexo != 'F'):
        sexo = str(input('Dados invalidos. Por gentileza informe seu sexo:')).upper()
print('Sexo {} registrado com sucesso. '.format(sexo))