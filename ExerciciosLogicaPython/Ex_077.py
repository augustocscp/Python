palavras = ('lis', 'gabrielle', 'augusto', 'sheylla', 'joao', 'anderson')
for v in palavras:
    print(f'Na palabvra {v} temos ', end='')
    if v.find('a') > 0:
        print('a ', end='')
    if v.find('e') > 0:
        print('e ', end='')
    if v.find('i') > 0:
        print('i ', end='')
    if v.find('o') > 0:
        print('o ', end='')
    if v.find('u') > 0:
        print('u ', end='')
    print('')