'Faça um Programa que leia três números e mostre o maior e o menor deles.'

#Coleta de informações
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o ultimo número: '))

#Verificando o maior
if (n1 > n2) and (n1 > n3):
    maior = n1
elif (n2 > n3):
    maior = n2
else:
    maior = n3

#Verificando o menor
if (n1 < n2) and (n1 < n2):
    menor = n1
elif (n2 < n3):
    menor = n2
else:
    menor = n3

print(f'O maior número digitado é o {maior:.0f}' )
print(f'O menor número digitado foi {menor:.0f}')