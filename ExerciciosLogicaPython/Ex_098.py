from time import sleep
def contador(inicio,fim, passo):
    if passo == 0:
        passo = -1
    if (inicio > fim) and (passo > 0):
        passo *= -1
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    for cont in range(inicio,fim,passo):
        print(cont, end=' ')
        sleep(0.1)
    print('FIM')
def format():
    print('-' * 50)


#PROGRAMA PRINCIPAL
format()
contador(1,10,1)
format()
contador(10,-1,-2)
format()

print('Agora é a sua vez de perssonalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
format()
contador(i,f,p)
