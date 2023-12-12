'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- INSS (8%) : R$
- IR (11%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

vlrHora = float(input('Qual o valor da hora trabalhada? '))
hrsTrab = float(input('Número de horas trabalhasdas? '))
totSal = vlrHora * hrsTrab
inss = totSal * 0.08
ir = (totSal - inss) * 0.11
sindicato = totSal * 0.05
totLiq = totSal - inss - ir - sindicato

print(f'+ Sálario bruto:    R$: {totSal:,.2f}')
print(f'- INSS:             R$: {inss:,.2f}')
print(f'- Imposto de renda: R$: {ir:,.2f}')
print(f'- Sindicato:        R$: {sindicato:,.2f}')
print(f'= Sálario Liquido:  R$: {totLiq:,.2f}')