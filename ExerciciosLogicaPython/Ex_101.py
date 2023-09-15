
def voto(nasc):

    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if (idade < 16):
        return f' Com {idade} anos. Não vota'
    elif (idade >= 16) and (idade < 18) or (idade > 70):
        return f'Com {idade} anos. Voto Opicional'
    elif (idade >= 18) and (idade < 70):
        return f'Com {idade} anos. Voto Obrigatorio'

nasc = int(input('Qual o ano de nascimento? '))
print(voto(nasc))