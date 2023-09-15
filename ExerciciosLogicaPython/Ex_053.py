frase = str(input('Digite uma frase: '))
frasec = (frase.replace(' ','')).upper()
palin = (frasec[::-1]).upper()
print(frasec)
print(palin)
print('O inverso de {} é {}'.format(frasec, palin))
if (frasec == palin):
    print('Temos um Palindromo')
else:
    print('Essa frase não é um palindromo')