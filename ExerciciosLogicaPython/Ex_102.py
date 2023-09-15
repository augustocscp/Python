def fatorial(n, show = False):
    """
    --> Calcula o fatoriakl de um número.
    :param n: O numero a ser calculado
    :param show: (Opicional) Mostrar ou não o calculo
    :return: O vair do fatorial de um número n.
    """
    f = 1
    if (show == True):
        for c in range(n, 0, -1):
            f *= c
            if (c > 1):
                print(c, 'x', end=' ')
            else:
                print(c, '=', end=' ')
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f

num = int(input('Digite o numero: '))
print('-'*50)
print(fatorial(num))
