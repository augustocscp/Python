from modulos import calculos

p = float(input('Digite o preço: '))
print(f'A metade de {p} é {calculos.metade(p,sep=True)}')
print(f'O dobro de {p} é {calculos.dobro(p,sep=True)}')
print(f'Aumentando 10%, temos {calculos.aumento(p,10,sep=True)}')