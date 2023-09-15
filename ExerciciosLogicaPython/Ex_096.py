def area(larg, comp):
    print(f'A área de um terreno {larg}X{comp} é de {(larg*comp)}m²')


print('Controle de Terrenos')
print('-'*20)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg,comp)