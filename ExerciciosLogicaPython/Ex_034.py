sal = float(input('Qual o seu salário? '))
aumento = 0
#Calculo de aumento. Abaixo de 1250,00 10% de aumento, acima disso 15%.
if (sal > 1.250):
    aumento = (sal * 0.1) + sal
else:
    aumento = (sal * 0.15) + sal
print('O seu salário passará de R${:.2f}, para R${:.2f}'.format(sal,aumento))

