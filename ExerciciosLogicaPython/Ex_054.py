from datetime import datetime
data = datetime.now()
maior = 0
menor = 0
for c in range(1,8):
    ano_nsc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if (data.year - ano_nsc) < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} maiores de idade e {} menores de idade'.format(maior, menor))

