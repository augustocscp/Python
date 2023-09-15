jogador = dict()
gol = list()
dados = list()

while True:
    n = 0
#CAPTAÇÃO DE DADOS
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input('Partidas jogadas: '))
    while (n != jogador['Partidas']):
        gol.append(int(input(f'Quantos gols na partida {n+1}: ')))
        n += 1
    jogador['Gols'] = gol[:]
    jogador['Total gols'] = sum(gol)
    jogador['Media de gols'] = (jogador['Total gols'] / jogador['Partidas'])
    gol.clear()
    dados.append(jogador.copy())
#FLAG DE CONTINUIDADE
    while True:
        resp = str(input('Deseja continuar? [S/N]' )).upper()[0]
        if resp in 'SN':
            break
        print('Resposta ERRADA! Responsa com S ou N!')
    if resp == 'N':
        break
#DEMONSTRAÇÃO DOS DADOS DOS JOGADORES EM TABELA
print('{:5}'.format('COD'),end='')
print('{:15}'.format('NOME'),end='')
print('{:15}'.format('GOLS'),end='')
print('{:5}'.format('TOTAL'))
print('-'*50)
for k,v in enumerate(dados):
    print('{:<5}{:15}{:15}{:5}'.format(k,v["Nome"],str(v["Gols"]),v["Total gols"]))
print('-'*50)
#FLAG PARA DETALHAR OS GOLS DE CADA JOGADOR
while True:
    busca = int(input('Deseja demonstrar os dados de qual jogador? [999 para parar] '))
    if (busca == 999):
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com o código {busca}! Tente novamente: ')
    else:#DEMONSTRAÇÃO DOS DADOS DO JOGADOR ESCOLHIDO
        print(f'-- Levantamento do jogador {busca} --')
        for k,v in enumerate(dados[busca]["Gols"]):
            print(f'No jogo {k} fez {v} gols.')
    print('-'*50)


