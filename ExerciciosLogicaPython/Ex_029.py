print(';====================================;')
print('         Camera de velocidade         ')
print(';====================================;')
vel = int(input('Qual a velocidade em que o carro está? '))
acima = (vel - 80)
multa = (acima * 7)
if (vel > 80):
    print('A velocidade do carro é de {}km/h! Ela está {}km/h acima da permitida! Você foi multado em R${:.2f} reais'.format(vel,(acima),multa))
else:
    print('Parabens, você está digirindo na velocidade da via!')