num = tuple(int(input('Digite um valor: ')) for c in range(5))
if num.count(9) > 0:
    print(f'O número 9 foi digitado {num.count(9)}x')
elif num.count(9) == 0:
    print(f'O número 9 não foi digitado')
if num.count(3) > 0:
    print(f'O número 3 foi digitado pela primeira vez na {num.index(3)+1}° posição ')
else:
    print(f'O número 3 não foi digitado!')
print('Os numeros pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, ' - ', end='')