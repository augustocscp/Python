jogador = dict()
gols = []
dados = []
while True:
    jogador.clear()
    n = totgols = 0
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input('Partidas jogadas: '))
    while (n != jogador['Partidas']):
        gols.append(int(input(f'Quantos gols na partida {n+1}: ')))
        n += 1
        totgols = sum(gols)
    jogador['Gols'] = gols
    jogador['Total gols'] = totgols
    jogador['Media de gols'] = (totgols / jogador['Partidas'])
    dados.append(jogador.copy())
    print(dados)
    while True:
        resp = str(input('Deseja continuar? [S/N]' )).upper()[0]
        if resp in 'SN':
            break
        print('Resposta ERRADA! Responsa com S ou N!')
    if resp == 'N':
        break


'''
print('-'*50)
print('{:^50}'.format('RESULTADO'))
print('-'*50)
print(f'Nome do jogador: {jogador["Nome"]}')
print(f'Jogou {jogador["Partidas"]} partidas')
print(f'Marcou {totgols} gols nessa temporada')
print(f'Uma media de {jogador["Media de gols"]:,.2f} gols por partida')'''