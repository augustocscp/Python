print('='*25)
print('   ANALISE DE CREDITO   ')
print('='*25)
nome = str(input('Qual o nome do comprador? '))
vlr_cs = int(input('Qual o valor a ser financiado? '))
sal = int(input('Qual o valor do salário do solicitante? '))
anos = int(input('O financiamento será em quantos anos? '))
teto = sal * 0.3
parcec = vlr_cs / (anos * 12)
print(parcec)
print()
if parcec <= teto:
    print('{} {} FINANCIAMENTO APROVADO {}'.format(' '*6, '\033[30:42m', '\033[m'))
    print('---- Condições do financiamento ----')
    print('Valor financiado: {}{}{:.2f}'.format(' '*7, '\033[1m', vlr_cs))
    print('Valor da parcela: {}{}{:.2f}'.format(' '*7, '\033[1m', parcec))
    print('Quantidade de parcelas:  {}{}'.format('\033[1m', (anos*12)))
    print('Vencimento das parcelas: {} 10° '.format('\033[1m'))
else:
    print('Nas condições apresentadas, o valor da parcela supera 30% do salário do solicitante.')
    print('Portanto, {}FINANCIAMENTO NEGADO{}'.format('\033[0:30:41m', '\033[m'))

