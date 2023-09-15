from modulos import calculos

p = float(input('Digite o preço: '))
print(f'A metade de {calculos.inicial(p,sep=True)} é {calculos.metade(p,sep=True)}')
print(f'O dobro de {calculos.inicial(p,sep=True)} é {calculos.dobro(p,sep=True)}')
print(f'Aumentando 10%, temos {calculos.aumento(p,10,sep=True)}')
print(f'Reduzindo 13%, temos {calculos.diminuir(p,13,sep=True)}')