listagem = list()
listagem_2 = list()
alunos = list()
notas = list()
nomes = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    m = (n1+n2)/2
    notas.append(n1)
    notas.append(n2)
    nomes.append(nome)
    alunos.append(nome)
    alunos.append(m)
    listagem.append(alunos[:])
    alunos.clear()
    listagem_2.append(notas[:])
    notas.clear()
    resp = input('Deseja continuar?[S/N] ').upper().strip()
    if resp == 'N':
        break
print('-'*50)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":<8}')
for l,c in enumerate(listagem):
    print(f'{l:<4}{c[0]:<10}{c[1]:<8}')
print('-'*50)
while True:
    resp2 = int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if resp2 == 999:
        break
    else:
        print(f'Notas de {nomes[resp2-1]} são {listagem_2[resp2-1]}')