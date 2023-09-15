def jogadores(n = 0,g = 0):
    return f'O jogador {n} fez {g} gol(s) no campeonato.'

nome = str(input('Nome do jogador: '))
if (nome == ''):
    nome = '<Desconhecido>'
gols = str(input('Número de gols: '))
if (gols == ''):
    gols = 0
print(jogadores(nome,gols))