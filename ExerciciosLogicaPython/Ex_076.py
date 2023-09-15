#precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,'Estojo', 25.00,'Transferidor', 4.20,'Compasso', 9.99,
#    'Mochila', 120.32,'Canetas', 22.30, 'Livro', 34.90)

precos = ('Lápis......................R$  1.75', 'Borracha...................R$  2.00', 'Caderno....................R$ 15.90',
          'Estojo.....................R$ 25.00', 'Transferidor...............R$  4.20', 'Compasso...................R$  9.99',
          'Mochila....................R$120.32', 'Canetas....................R$ 22.30', 'Livro......................R$ 34.90')
print('-'*35)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-'*35)
for n in precos:
    print(n)
print('-'*35)

