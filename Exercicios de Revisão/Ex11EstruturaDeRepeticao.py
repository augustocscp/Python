
'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
de anos necessários para que a população do país A ultrapasse ou iguale a população
 do país B, mantidas as taxas de crescimento.'''

paisA = 8000
paisB = 200000
tempo = 0

while paisB >= paisA:
    paisA += paisA * 0.3
    paisB += paisB * 0.015
    tempo += 1
print(f'Levará {tempo+1} anos para que o pais A ultrapasse a população do pais B em numéro de habitantes.')