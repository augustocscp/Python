print('=================================')
print('Calculadora de passagem de ônibus')
print('=================================')
local = str(input('Para onde você deseja viajar? '))
dist = int(input('Quantos KM tem de brasilia até {}? '.format(local)))
if (dist <= 200):
    print('Sua passagem para {} irá custar R${} reais'.format(local,dist * 0.50))
else:
    print('Sua passagem para {} irá custar R${} reais'.format(local,dist * 0.45))