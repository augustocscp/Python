def notas(*n, sit=False):
    """
    --> Função para analisar notas e situççoes ded varios alunos.
    :param n: Uma ou mais notas dos alunos (aceita varias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação final da media do aluno.
    :return: Dicionario com varias informações sobre a situação da turma.
    """
    dados = dict()
    media = sum(n)/ len(n)
    maior = max(n)
    menor = min(n)
    situação = ''
    if (sit == False):
        dados = {'Total': len(n), 'Maior': maior, 'Menor': menor, 'Media': media}
    elif (sit == True):
        if (media < 5):
            situação = 'Ruim'
        elif (media >= 5) and (media < 7):
            situação = 'Razoavel'
        elif (media >= 7) and (media < 8.9):
            situação = 'Boa'
        else:
            situação = 'Otimo'
        dados = {'Total': len(n), 'Maior': maior, 'Menor': menor, 'Media': media, 'Situação': situação}
    return dados


resp = notas(5.5,2.5,10,6.5)
print(resp)

