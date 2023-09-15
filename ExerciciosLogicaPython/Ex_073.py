tabela = ('Botafogo', 'Palmeiras', 'Cruzeiro', 'Fortalza', 'São Paulo', 'Fluminence', 'Grêmio', 'Internacional', 'Bahia',
          'Atletico-PR', 'Vasco da Gama', 'Bragantino', 'Cuiabá', 'Santos', 'Corinthians', 'Atlético-MG', 'Flamengo', 'Goias',
          'Coritiba', 'América-MG')
print('-'*30)
print(f'Os primeiros cinco colocados: {tabela[1:6]}')
print('-'*30)
print(f'Os ultimos cinco colocados: {tabela[15:]}')
print('-'*30)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('-'*30)
print(f'O Corinthians está na {tabela.index("Corinthians")}° posição na tabela!')
