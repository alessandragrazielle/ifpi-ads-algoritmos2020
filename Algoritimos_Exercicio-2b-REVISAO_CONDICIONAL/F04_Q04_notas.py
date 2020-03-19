nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))


media = (nota1 + nota2) / 2


def aprovacao():
    if media == 10:
        print('APROVADO COM DISTINÇÃO!')
    elif media >= 7:
        print('APROVADO!')
    else :
        print('REPROVADO!')


aprovacao()