
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
de anos necessários para que a população do país A ultrapasse ou iguale a população
do país B, mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.

 '''

tempo = 0;

while True:

    # Entrada e validação de dados
    paisA = float(input("Informe o tamanho da população A: "))
    taxaA = float(input("Informe a taxa de crescimento da população A: "))
    while True:
        paisB = float(input("Informe o tamanho da população b: "))
        if (paisB > paisA):
            break;
        print('O população B não pode ser menor ou igual a população A')

    while True:
        taxaB = float(input("Informe a taxa de crescimento da população B: "))
        if (taxaB < taxaA):
            break;
        print('O taxa de crescimento da população B não pode ser maior ou igual a população A')

    # Calculo
    while paisB >= paisA:
        paisA += paisA * 0.03
        paisB += paisB * 0.015
        tempo += 1

    # Retorno
    print(f'Levará {tempo} anos para que o pais A ultrapasse a população do pais B em numéro de habitantes.')


    # Interruptor
    while True:
        resp = str(input("Deseja continuar? [Sim ou Não]")).upper()[0]
        if (resp in 'SN'):
            break
        print("ERRO! Apenas Sim ou Não! ")

    if resp == 'N':
        print("Fim do programa! Até a proxima.")
        break
