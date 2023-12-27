
'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''


while True:
    nome = str(input('Usuario: '))
    senha = str(input('Senha: '))

    if nome != senha:
        break;
    print('Erro! A senha não pode ser igual ao usuario!');

print('Usuario cadastrado com sucesso!')