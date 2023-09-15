frase = str(input('Digite uma frase: ')).strip()
print('A letra "a" aparece {} vezes na frase digitada.'.format(frase.lower().count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.lower().find('a')+1))
print('E pela ultima vez na posição {}'.format(frase.lower().rfind('a')+1))